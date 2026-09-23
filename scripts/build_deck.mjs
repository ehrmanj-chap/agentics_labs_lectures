/** Rebuild the editable deck from data/slides.json.
 * Requires @oai/artifact-tool. Run a copy from a private build folder whose
 * node_modules link resolves that package, passing REPO_DIR and BUILD_DIR.
 * Writes candidate.pptx; validate and render before replacing the download.
 */
import fs from 'node:fs/promises';
import path from 'node:path';
import { Presentation, PresentationFile } from '@oai/artifact-tool';
const root=process.env.REPO_DIR;
const build=process.env.BUILD_DIR;
if(!root||!build) throw new Error('Set absolute REPO_DIR and BUILD_DIR');
const slides=JSON.parse(await fs.readFile(path.join(root,'data/slides.json'),'utf8'));
const model=JSON.parse(await fs.readFile(path.join(root,'data/model-snapshot.json'),'utf8'));
const size=JSON.parse(await fs.readFile(path.join(root,'data/model-sizes.json'),'utf8'));
const P=Presentation.create({slideSize:{width:1280,height:720}});
const RED='#7a0019', INK='#222222', MUTED='#5d5d5d', PALE='#f8f2f3';
const FONT='DejaVu Serif', SANS='DejaVu Sans';
function text(s,t,x,y,w,h,px=30,color=INK,bold=false,align='left',font=FONT){
 const shape=s.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 shape.text=t; shape.text.style={typeface:font,fontSize:px,color,bold,alignment:align,autoFit:'none',insets:{left:0,right:0,top:0,bottom:0}}; return shape;
}
async function img(s,file,x,y,w,h,alt){
 const ext=path.extname(file),mime=ext==='.webp'?'image/webp':ext==='.jpg'?'image/jpeg':'image/png';
 s.images.add({blob:new Uint8Array(await fs.readFile(path.join(root,'assets',file))),contentType:mime,alt,fit:'contain',position:{left:x,top:y,width:w,height:h}});
}
function footer(s,i,color=MUTED){text(s,'Chapman Agentics Labs',64,679,900,25,16,color);text(s,String(i+1).padStart(2,'0'),1140,679,76,25,16,color,false,'right');}
function title(s,t){text(s,t,64,44,1152,112,t.length>40?42:46,RED,true);}
function aside(s,t,y=596){if(t)text(s,t,72,y,1136,68,23,RED);}
function chart(s,items,key,max){
 const score=key==='score';
 const c=s.charts.add('bar',{
  position:{left:68,top:156,width:1138,height:385},
  categories:items.map(m=>m.name+(score?' ($'+m.price.toFixed(3)+')':'')),
  series:[{name:score?'Composite benchmark score':'Total parameters, billions',values:items.map(m=>m[key]),fill:RED}],
  barOptions:{direction:'bar',grouping:'clustered',gapWidth:55},hasLegend:false,
  chartFill:'#ffffff',chartLine:{fill:'none',width:0},plotAreaFill:'#ffffff',plotAreaLine:{fill:'none',width:0},
  xAxis:{visible:true,min:0,max,majorUnit:score?10:100,textStyle:{typeface:SANS,fontSize:20,fill:MUTED},line:{fill:'#dddddd',width:1},majorGridlines:{fill:'#dddddd',width:1}},
  yAxis:{visible:true,textStyle:{typeface:SANS,fontSize:score?19:22,fill:MUTED},line:{fill:'#dddddd',width:1},majorGridlines:null},
  dataLabels:{showValue:true,position:'outEnd',textStyle:{typeface:SANS,fontSize:22,bold:true,fill:INK}}
 });
 return c;
}
for(let i=0;i<slides.length;i++){
 const d=slides[i],s=P.slides.add();s.background.fill='#ffffff';
 s.speakerNotes.textFrame.setText(d.notes+(d.sources.length?'\n\nSources\n'+d.sources.join('\n'):''));
 if(d.kind==='cover'){
  s.background.fill='linear(180deg, #7a0019 0%, #8e122d 100%)';
  text(s,'Chapman Agentics Labs',64,64,1152,40,25,'#ffffff',false,'center');
  text(s,d.title,64,198,1152,100,70,'#ffffff',true,'center');
  text(s,d.subtitle,64,316,1152,50,33,'#ffffff',false,'center');
  text(s,'Jordan Ehrman',64,455,1152,46,34,'#ffffff',true,'center');
  text(s,'Riverbot Agentics',64,502,1152,40,28,'#ffffff',false,'center');
  text(s,'Business students + anyone curious',64,589,1152,40,24,'#ffffff',false,'center');
  await img(s,'riverbot-logo.png',1140,570,76,76,'Riverbot Agentics logo');
 }else if(d.kind==='transition'){
  s.background.fill=PALE;
  text(s,d.title,80,77,1100,150,d.title.length>38?49:56,RED,true);
  const start=d.title.length>38?259:239;
  d.body.forEach((t,j)=>text(s,t,80,start+j*108,1100,96,j===0?34:30,j===0?RED:INK));
  aside(s,d.aside,590);footer(s,i);
 }else if(d.kind==='finale'){
  await img(s,'go-do-your-lab.png',160,16,960,495,'GO DO YOUR LAB in rainbow WordArt');
  text(s,d.body[0],80,524,1120,50,30,RED,true,'center');
  text(s,d.body[1],80,579,1120,44,25,INK,false,'center');
  text(s,d.body[2],80,634,1120,40,25,RED,false,'center');
 }else{
  title(s,d.title);footer(s,i);
  if(d.kind==='reddit'){
   await img(s,d.image,630,161,586,425,'Conversation screenshot: '+d.quote+' / '+d.answer);
   text(s,d.quote,72,173,515,135,30,RED,true);
   text(s,d.answer,72,314,515,113,28,INK);
   d.body.forEach((t,j)=>text(s,t,72,443+j*81,515,78,24,INK,false,'left',FONT));
   aside(s,d.aside,621);
  }else if(d.kind==='score'){
   chart(s,model.models,'score',70);
   text(s,'Composite score (higher is better; not a percentage)',72,563,1136,38,25,INK);
   text(s,'Labels: blended API USD / 1M tokens. PantherAI is free to students.',72,605,1136,34,21,MUTED);
   text(s,'Selected LLM Stats data · 22 Sep 2026 · Models shown are not the campus menu.',72,642,1136,26,16,MUTED);
  }else if(d.kind==='size'){
   chart(s,size.models,'total',800);
   text(s,'Total parameters, billions',72,552,1136,40,27,INK);
   text(s,'Active subset: gpt-oss-120b 5.1B / DeepSeek-R1 37B',72,597,1136,37,25,RED);
   text(s,'Size alone does not determine quality. Closed-model sizes often remain undisclosed.',72,641,1136,26,19,MUTED);
  }else if(d.kind==='access'){
   text(s,d.body[0],72,177,1136,70,44,RED,true,'left',SANS);
   d.body.slice(1).forEach((t,j)=>text(s,`${j+1}.  ${t}`,72,294+j*79,1136,65,32));
   aside(s,d.aside);
  }else if(d.kind==='demo'){
   text(s,d.quote,72,168,1136,85,35,RED,true);
   d.body.forEach((t,j)=>text(s,t,72,291+j*93,1136,83,31));
   aside(s,d.aside);
  }else if(d.kind==='ecosystem'){
   d.body.forEach((t,j)=>text(s,t,72,186+j*115,1136,100,33));
   aside(s,d.aside,566);
  }else{
   const step=d.kind==='loop'?77:92;
   d.body.forEach((t,j)=>text(s,t,72,180+j*step,1136,step-8,d.kind==='loop'?29:31));
   aside(s,d.aside,599);
  }
 }
}
await fs.mkdir(build,{recursive:true});
await (await PresentationFile.exportPptx(P)).save(path.join(build,'candidate.pptx'));
await fs.writeFile(path.join(build,'deck-inspection.ndjson'),(await P.inspect({kind:'slide,textbox,chart,image',maxChars:200000})).ndjson);
console.log(`Built ${slides.length} editable slides at ${path.join(build,'candidate.pptx')}`);
