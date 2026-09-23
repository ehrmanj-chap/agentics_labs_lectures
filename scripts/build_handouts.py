"""Build student and instructor PDFs from data/lab.json. Requires ReportLab."""
from pathlib import Path
import json,re
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
ROOT=Path(__file__).resolve().parents[1]
LAB=json.loads((ROOT/'data/lab.json').read_text())
OUT=ROOT/'downloads';OUT.mkdir(exist_ok=True)
FONT=Path('/usr/share/fonts/truetype/dejavu')
for name,file in [('Serif','DejaVuSerif.ttf'),('SerifBold','DejaVuSerif-Bold.ttf')]:pdfmetrics.registerFont(TTFont(name,str(FONT/file)))
RED=HexColor('#7a0019');INK=HexColor('#222222');MUTED=HexColor('#5d5d5d');PALE=HexColor('#f8f2f3');LINE=HexColor('#cfc7c9')
W,H=612,792;L=43;CW=526

def clean(s):return s.replace('–','-').replace('—','-').replace('−','-').replace('→','then')
def p(c,t,x,y,w=CW,size=9.8,leading=14,color=INK,bold=False):
 st=ParagraphStyle('p',fontName='SerifBold' if bold else 'Serif',fontSize=size,leading=leading,textColor=color)
 obj=Paragraph(escape(clean(t)),st);_,h=obj.wrap(w,720);obj.drawOn(c,x,y-h);return y-h

def head(c,tag,title,page,total):
 c.setFillColor(RED);c.rect(0,H-118,W,118,fill=1,stroke=0)
 p(c,'CHAPMAN AGENTICS LABS  /  '+tag,L,H-29,size=9,leading=12,color=HexColor('#ffffff'))
 p(c,title,L,H-55,size=24,leading=30,color=HexColor('#ffffff'),bold=True)
 c.setFillColor(MUTED);c.setFont('Serif',8)
 c.drawString(L,28,'Jordan Ehrman · Riverbot Agentics')
 c.drawRightString(W-L,28,f'{page} / {total}')
 return H-138

def section(c,title,y,size=15):return p(c,title,L,y,size=size,leading=size+5,color=RED,bold=True)-7

def lines(c,y,count=3):
 c.setStrokeColor(LINE);c.setLineWidth(.5)
 for i in range(count):c.line(L,y-i*18,W-L,y-i*18)
 return y-count*18

def student():
 c=canvas.Canvas(str(OUT/'Lab_1_Student_Handout.pdf'),pagesize=(W,H));c.setTitle('Lab 1 - Plan the club lunch: student handout');c.setAuthor('Jordan Ehrman / Riverbot Agentics')
 y=head(c,'LAB 01 · 20 MINUTES','Plan the club lunch',1,2)
 y=p(c,'Use your own words with a chatbot. Work individually or in pairs, in one conversation. Spend about five minutes on each part. Multiple menus can work.',L,y)-9
 y=p(c,'Name(s), app and model: __________________________________________________',L,y,size=9)-12
 y=p(c,LAB['rules'],L,y,size=9.3,leading=13)-17
 for idx in [0,1]:
  part=LAB['parts'][idx];y=section(c,f"{idx+1}. {part['title']}   /   {part['time']}",y)
  y=p(c,part['facts'],L,y)-7
  # Keep the handout open-ended and concise, with the full task on the web.
  task=['Propose an order with your chatbot. Decide what it needs to know and what you would check before committing.','Update the same conversation. Check the revised order against the new facts and the earlier requirements.'][idx]
  y=p(c,task,L,y)-7
  y=p(c,'Your record: '+part['record'],L,y,size=9.2,leading=13,color=RED)-19
  y=lines(c,y,3)-17
 if y<40:raise ValueError(f'Student page 1 overflow: {y}')
 c.showPage();y=head(c,'LAB 01 · CONTINUED','When the plan changes',2,2)
 for idx in [2,3]:
  part=LAB['parts'][idx];y=section(c,f"{idx+1}. {part['title']}   /   {part['time']}",y)
  y=p(c,part['facts'],L,y)-8
  task=['Explore a workable proposal. Decide what you can settle now and what still needs a person to confirm. Keep all earlier constraints in view.','Finish a short proposal with quantities, cost and pickup details. Check all the facts, then reflect on the conversation.'][idx-2]
  y=p(c,task,L,y)-8
  y=p(c,'Your record: '+part['record'],L,y,size=9.2,leading=13,color=RED)-19
  y=lines(c,y,3 if idx==2 else 4)-20
 y=p(c,'No chatbot? Take turns proposing and checking the plans with a partner. Submit your four short records wherever your instructor specifies.',L,y,size=8.5,leading=12,color=MUTED)
 if y<42:raise ValueError(f'Student page 2 overflow: {y}')
 c.save()

def block(c,label,value,y):
 y=p(c,label.upper(),L,y,size=9,leading=12,color=RED,bold=True)-4
 return p(c,value,L,y,size=10,leading=15)-14

def teacher():
 c=canvas.Canvas(str(OUT/'Lab_1_Instructor_Cookbook.pdf'),pagesize=(W,H));c.setTitle('Lab 1 - Instructor cookbook');c.setAuthor('Jordan Ehrman / Riverbot Agentics')
 y=head(c,'INSTRUCTOR COPY','Your on-screen cookbook',1,4)
 y=p(c,'Human Agent Loop / Plan the club lunch',L,y,size=15,leading=21,color=RED,bold=True)-10
 y=p(c,'About 18 minutes of teaching and demo, followed by 20 minutes of student work. This follows the Microsoft guest session on prompting.',L,y,size=11,leading=16)-21
 y=section(c,'Five-minute prep',y)
 for t in ['Open a fresh chatbot conversation and note the model. Keep the lecture, this guide and the prepared demo in separate tabs.','Have the student page or two-page handout ready. Students choose their own wording; the sample messages in this guide are for your demo.','Read the four turns once. A sample route costs $180, then $200, then $188 with pickup. Several other menus are valid.']:
  y=p(c,t,L,y)-11
 y=section(c,'Run of show',y-6)
 for time,activity in [('0-3','Introduce yourself and get a chatbot open.'),('3-5','App, model, tools and the two comparison charts.'),('5-8','Four Reddit moments; ask the room to spot the gap.'),('8-12','Run the four-turn lunch demo, about one minute per part.'),('12-18','Debrief, name the loop, explain the lab and close.'),('18-38','Student work: four parts, about five minutes each.')]:
  p(c,time,L,y,70,size=10,color=RED,bold=True);y=p(c,activity,L+75,y,CW-75,size=10,leading=15)-10
 y=section(c,'If the live demo gets weird',y-8)
 y=p(c,'A mistake is useful material: pause and check it with the room. If login or generation stalls, open lab1/demo.html and show the prepared response for that part. After two minutes of login trouble, pair students up.',L,y,size=10,leading=15)
 if y<45:raise ValueError(f'Teacher page 1 overflow {y}')
 c.showPage()
 for page,ids in [(2,[0,1]),(3,[2,3])]:
  y=head(c,'LIVE DEMO · ABOUT 1 MINUTE PER PART','One conversation, four turns',page,4)
  for idx in ids:
   part=LAB['parts'][idx]
   y=section(c,str(idx+1)+'. '+part['title'],y)
   y=block(c,'Type or say',part['teacher_prompt'],y)
   y=block(c,'Say to the room',part['teacher_say'],y)
   y=block(c,'Look for',part['teacher_check'],y)
   y=p(c,'If needed: '+part['teacher_followup'],L,y,size=8.8,leading=12,color=MUTED)-18
  if y<44:raise ValueError(f'Teacher page {page} overflow {y}')
  c.showPage()
 y=head(c,'ANSWER KEY + DEBRIEF','More than one menu works',4,4)
 y=p(c,'Let C be the number of chicken sandwiches. The remaining meals are vegetarian wraps. Every guest also receives a $1 drink.',L,y,size=10.5,leading=16)-18
 for title,formula,detail in [('24 guests, with delivery','$156 + C','0-24 chicken sandwiches fit the initial budget. Dietary needs, stock and timing still need checking.'),('30 guests, with delivery','$192 + C','0-8 chicken sandwiches fit. At least 22 meals must be wraps to stay within $200.'),('30 guests, with pickup','$180 + C','0-18 chicken sandwiches fit. Stock is now the tighter limit. Pickup still needs confirmation in Part 3.')]:
  y=p(c,title+'   /   '+formula,L,y,size=12,leading=17,color=RED,bold=True)-5
  y=p(c,detail,L,y,size=10,leading=15)-16
 y=p(c,'Valid final examples: 8 chicken + 22 wraps + 30 drinks = $188; 18 chicken + 12 wraps + 30 drinks = $198; 30 wraps + 30 drinks = $180. Pickup removes the delivery fee. Students may keep an earlier menu.',L,y,size=10,leading=15)-20
 y=section(c,'Before calling the plan finished',y)
 for t in ['30 meals and 30 drinks; at least 8 wraps; no more than 18 chicken sandwiches.','Total of $200 or less, including any fees.','Confirmed 11:15 a.m. pickup and arrival before noon.','A checked proposal with no claim that anyone placed an order.']:
  y=p(c,t,L,y,size=10,leading=15)-8
 y=section(c,'While they work, then debrief',y-5)
 y=p(c,'At each five-minute mark, invite students to the next part. Ask which facts carried forward and what is still an assumption. If time allows, hear one useful response and one human check from the room. Accept different menus that meet the constraints. A caught and explained model error is useful evidence.',L,y,size=10,leading=15)-12
 y=p(c,'A person supplies the facts in this exercise. A connected agent would need tools and permissions to act. Students submit four short records and the model name; no prescribed prompt, loop diagram or full transcript is required.',L,y,size=9,leading=13,color=MUTED)
 if y<42:raise ValueError(f'Teacher page 4 overflow {y}')
 c.save()
student();teacher();print('Built student handout (2 pages) and instructor cookbook (4 pages).')
