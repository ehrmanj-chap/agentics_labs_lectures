"""Check shared lesson content, local links and the lunch arithmetic. No dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json, re, subprocess, zipfile
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
def load(name):return json.loads((ROOT/'data'/name).read_text())
lab,slides,demo=load('lab.json'),load('slides.json'),load('demo-steps.json')
assert lab['duration']==20 and len(lab['parts'])==len(demo)==4
assert len(slides)==20
for part,step in zip(lab['parts'],demo):
 assert part['title']==step['title'] and part['facts']==step['observation'] and part['teacher_check']==step['action']
# Rebuilding the shared pages should not change any checked-in output.
outputs=['lab1/lecture-data.js','lab1/demo-data.js','lab1/index.html','lab1/demo.html','lab1/instructor.html','lab1/instructor-notes.md','lab1/worksheet.md']
before={p:(ROOT/p).read_bytes() for p in outputs}
subprocess.run(['python3',str(ROOT/'scripts/sync_data.py')],check=True,capture_output=True)
assert all((ROOT/p).read_bytes()==data for p,data in before.items()), 'Generated teaching pages were stale'
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.append(a['id'])
  for k in ['href','src']:
   if a.get(k):self.links.append(a[k])
for page in ROOT.rglob('*.html'):
 doc=Links();doc.feed(page.read_text());assert len(doc.ids)==len(set(doc.ids)),f'Duplicate IDs: {page}'
 for link in doc.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  target=(page.parent/unquote(u.path)).resolve() if u.path else page
  assert target.is_file(),f'Broken link: {page} -> {link}'
  if u.fragment and target.suffix=='.html':
   other=Links();other.feed(target.read_text());assert u.fragment in other.ids,f'Missing anchor: {link}'
 stale=re.search(r'museum|River prints|Garden prints|LOOKUP_INVENTORY|30-minute schedule',page.read_text(),re.I)
 assert not stale,f'Old lab wording: {page}'
# Enumerate all integer menus; check the budget and stock boundaries independently.
def feasible(people,delivery,stock,veg):
 return [c for c in range(people+1) if c<=stock and people-c>=veg and 6*c+5*(people-c)+people+delivery<=200]
assert feasible(24,12,24,0)==list(range(25))
assert feasible(30,12,18,8)==list(range(9))
assert feasible(30,0,18,8)==list(range(19))
assert 8*6+22*5+30==188 and 18*6+12*5+30==198
ppt=ROOT/'downloads/Lab_1_Human_Agent_Loop.pptx'
ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
with zipfile.ZipFile(ppt) as z:
 slideparts=[n for n in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml',n)]
 assert len(slideparts)==20
 for i,s in enumerate(slides,1):
  xml=ET.fromstring(z.read(f'ppt/slides/slide{i}.xml'))
  text=' '.join(n.text or '' for n in xml.findall('.//a:t',ns))
  assert s['title'] in text or s['kind']=='finale',(i,'Title missing')
  notes=' '.join(n.text or '' for n in ET.fromstring(z.read(f'ppt/notesSlides/notesSlide{i}.xml')).findall('.//a:t',ns))
  assert s['notes'] in notes,(i,'Speaker notes differ')
  assert not re.search(r'museum|Garden prints|River prints|\$213',text+notes,re.I)
print('PASS: 20 matching slide notes, 4 matching parts, generated-file parity, local links, IDs, old-content scan and all feasible lunch menus.')
