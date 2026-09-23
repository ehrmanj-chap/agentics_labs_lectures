const fields = [...document.querySelectorAll('#worksheet textarea')];
const storageKey = 'riverbot-lab1-lunch-v2';
const saveStatus = document.querySelector('#status');
try {
  const draft = JSON.parse(localStorage.getItem(storageKey) || '{}');
  fields.forEach(field => { field.value = draft[field.name] || ''; });
} catch { saveStatus.textContent = 'Browser saving unavailable. Use Download.'; }
function save() {
  try {
    localStorage.setItem(storageKey, JSON.stringify(Object.fromEntries(fields.map(f => [f.name, f.value]))));
    saveStatus.textContent = 'Saved in this browser.';
  } catch { saveStatus.textContent = 'Browser saving unavailable. Use Download.'; }
}
fields.forEach(field => field.addEventListener('input', save));
document.querySelector('#print').onclick = () => {
  fields.forEach(field => {
    const previous = field.parentElement.querySelector('.print-response');
    if (previous) previous.remove();
    const response = document.createElement('div');
    response.className = 'print-response print-only';
    response.textContent = field.value || '[Not filled]';
    field.after(response);
  });
  window.print();
};
document.querySelector('#download').onclick = () => {
  let output = '# Lab 1 — Plan the club lunch\n\nJordan Ehrman · Riverbot Agentics\n';
  fields.forEach(field => {
    const label = document.querySelector('label[for="' + field.id + '"]').textContent;
    output += '\n## ' + label + '\n\n' + (field.value || '[Not filled]') + '\n';
  });
  const url = URL.createObjectURL(new Blob([output], { type: 'text/markdown' }));
  const link = document.createElement('a');
  link.href = url;
  link.download = 'Lab_1_My_Lunch_Plan.md';
  link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
  saveStatus.textContent = 'Worksheet downloaded.';
};
document.querySelector('#clear').onclick = () => {
  if (confirm('Clear your saved worksheet on this browser? Download a copy first if you need it.')) {
    fields.forEach(field => { field.value = ''; });
    try { localStorage.removeItem(storageKey); } catch {}
    saveStatus.textContent = 'Draft cleared.';
  }
};
