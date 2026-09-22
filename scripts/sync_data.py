"""Refresh browser data from the editable JSON sources. No dependencies."""
from pathlib import Path
import json
root = Path(__file__).resolve().parents[1]
def declaration(name, file):
    data = json.loads((root / 'data' / file).read_text())
    return 'const ' + name + '=' + json.dumps(data, ensure_ascii=False) + ';\n'
(root / 'lab1' / 'lecture-data.js').write_text(
    declaration('slides', 'slides.json') + declaration('modelData', 'model-snapshot.json')
    + declaration('sizeData', 'model-sizes.json'))
(root / 'lab1' / 'demo-data.js').write_text(declaration('demoSteps', 'demo-steps.json'))
