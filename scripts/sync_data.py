"""Refresh browser data from the editable JSON sources. No dependencies."""
from pathlib import Path
import json
import html
import re
root = Path(__file__).resolve().parents[1]
def declaration(name, file):
    data = json.loads((root / 'data' / file).read_text())
    return 'const ' + name + '=' + json.dumps(data, ensure_ascii=False) + ';\n'
(root / 'lab1' / 'lecture-data.js').write_text(
    declaration('slides', 'slides.json') + declaration('modelData', 'model-snapshot.json')
    + declaration('sizeData', 'model-sizes.json'))
(root / 'lab1' / 'demo-data.js').write_text(declaration('demoSteps', 'demo-steps.json'))

# Keep the printable and browser instructor notes in the same slide order.
slides = json.loads((root / 'data' / 'slides.json').read_text())
notes_md = '\n\n'.join(
    f"## Slide {number} — {slide['title']}\n\n{slide['notes']}"
    for number, slide in enumerate(slides, 1)
)
notes_html = '\n'.join(
    '<section class="paper"><p class="eyebrow">Slide ' + str(number)
    + '</p><h2>' + html.escape(slide['title']) + '</h2><p>'
    + html.escape(slide['notes']) + '</p></section>'
    for number, slide in enumerate(slides, 1)
)
for filename, content in [('instructor-notes.md', notes_md), ('instructor.html', notes_html)]:
    path = root / 'lab1' / filename
    path.write_text(re.sub(
        r'<!-- SLIDE_NOTES_START -->.*?<!-- SLIDE_NOTES_END -->',
        lambda _: '<!-- SLIDE_NOTES_START -->\n' + content + '\n<!-- SLIDE_NOTES_END -->',
        path.read_text(), flags=re.S,
    ))
