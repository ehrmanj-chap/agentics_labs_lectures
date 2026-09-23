let part = 0;
function show() {
  const step = demoSteps[part];
  document.getElementById('beat').textContent = `Part ${part + 1} of ${demoSteps.length}`;
  const output = document.getElementById('demo-output');
  output.replaceChildren();
  const heading = document.createElement('h2');
  heading.textContent = step.title;
  output.append(heading);
  for (const [key, label] of [['observation', 'New facts'], ['state', 'What we know now'], ['action', 'One possible response'], ['stop', 'Continue or stop?']]) {
    const h = document.createElement('h3');
    h.className = 'demo-label';
    h.textContent = label;
    const p = document.createElement('p');
    p.textContent = step[key];
    output.append(h, p);
  }
  document.getElementById('back').disabled = part === 0;
  const next = document.getElementById('advance');
  next.disabled = part === demoSteps.length - 1;
  next.textContent = next.disabled ? 'Plan complete' : `Show part ${part + 2}`;
}
document.getElementById('back').onclick = () => { part = Math.max(0, part - 1); show(); };
document.getElementById('advance').onclick = () => { part = Math.min(demoSteps.length - 1, part + 1); show(); };
document.getElementById('reset').onclick = () => { part = 0; show(); };
show();
