# Agentics Labs & Lectures

Hands-on AI and agentics labs with **Jordan Ehrman · Riverbot Agentics**. Built for business students and open to anyone curious.

## Lab 1: Human Agent Loop

A school wants 24 prints from a museum. Students choose a chat model, act as its tool operator, introduce changing inventory and delivery constraints, and audit the model’s next action and stopping behavior.

- **Teaching:** about 18 minutes, including login, a two-minute model ecosystem overview, four real Reddit examples, and a three-minute demo.
- **Student lab:** 30 minutes; pairs or groups of 3–4; solo also works.
- **Prerequisites:** a browser. No coding or paid personal AI plan required.
- **Position in the course:** follows the Microsoft guest session on prompting. This lab studies the agent loop; it does not repeat that prompting lecture.

## Open the materials

Download this repository and open `index.html` in a browser. The lecture, demo and worksheet are static files; no installation or API key is needed. External AI portals and source links require internet access. If browser clipboard or local saving is unavailable, select the starter manually and download the worksheet.

| Material | File |
| --- | --- |
| Course home | [index.html](index.html) |
| Browser presentation | [lab1/lecture.html](lab1/lecture.html) |
| Editable PowerPoint, with speaker notes | [Lab_1_Human_Agent_Loop.pptx](downloads/Lab_1_Human_Agent_Loop.pptx) |
| Student lab + local worksheet | [lab1/index.html](lab1/index.html) |
| Interactive scripted demo | [lab1/demo.html](lab1/demo.html) |
| Instructor run-of-show + answer key | [lab1/instructor.html](lab1/instructor.html) |
| Plain-text speaker notes | [lab1/instructor-notes.md](lab1/instructor-notes.md) |
| Blank worksheet | [lab1/worksheet.md](lab1/worksheet.md) |
| Sources and credits | [lab1/sources.html](lab1/sources.html) |
| Recovered 15-lab sequence | [COURSE_MAP.md](COURSE_MAP.md) |

For a local web server, run `python3 -m http.server 8000` from this directory and open `http://localhost:8000`. The root directory is also ready for static hosting, including GitHub Pages. No hosting service is configured by this repository.

### Presenting

Use the arrow buttons or keyboard arrows to navigate. Toggle **Speaker notes** when needed. On the final WordArt slide, click **A quick thing before you go** to reveal the closing message. The PowerPoint uses a static final slide and contains the spoken transition in its notes. Use the browser lecture for the animated reveal.

### Chapman access

The model portal is **[PantherAI](https://pantherai.chapman.edu/login)**. Choose **Chapman SSO Login** and sign in with a Chapman account. Chapman identifies active students, faculty and staff as eligible, and the Library describes access as free. **PantherBot** is the separate campus-help chatbot. Model choices vary; record the model actually shown in the menu. Visiting participants can pair up, use an existing free chat account, or use the offline trace.

### Lab behavior

The demo is explicitly scripted, not a live AI backend. Students can run the provided starter and observations in any available chat model. Tools are simulated by people. No purchase, message, or reservation is made. The final approved quote is **24 Garden prints × $7 + $45 rush shipping = $213**. The model should stop after drafting the approved quote.

The worksheet stays in the student’s browser and can be downloaded as Markdown. This site does not collect submissions. Students submit wherever their instructor specifies.

## Editing and evidence

The site uses plain HTML, CSS and JavaScript with no production dependencies or build step. Slide content is in `data/slides.json`; model evidence is in `data/model-snapshot.json` and `data/model-sizes.json`. Run `python3 scripts/sync_data.py` after changing slide or demo JSON to refresh the browser data files. The browser lecture now has 20 slides, including six transition slides. The sync script also refreshes both instructor-note formats. **Draft status:** the checked-in PowerPoint is still the original 14-slide version; its matching revision must be uploaded before this branch is ready to merge. PowerPoint is an editable delivery artifact; its charts include native editable data.

Research snapshot: **September 22, 2026**. Public login and access guidance were checked; the authenticated PantherAI student menu was not inspected. The LLM Stats chart is a selected price/ability snapshot, not a campus availability list or a permanent ranking. The second chart illustrates disclosed parameter counts. Reddit screenshots are historical anecdotes, not model benchmarks.

The burgundy gradient, Georgia typography, centered header, white cards and site icon match [Chapman Cultural Agents](https://github.com/ehrmanj-chap/chapman-cultural-agents). Riverbot appears as the presenter and consulting identity. The original logo and contact come from [Riverbot Agentics](https://github.com/ehrmanj-chap/riverbot-agentics). Source links, qualifications and image credits are in the sources page and slide notes. Third-party images and brand assets retain their respective ownership; no blanket license is asserted over them.

Contact: **riverbotagentics@gmail.com**
