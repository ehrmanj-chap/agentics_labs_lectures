# Agentics Labs & Lectures

Hands-on AI labs with **Jordan Ehrman · Riverbot Agentics**. Built for business students and open to anyone curious.

## Lab 1: Human Agent Loop — Plan the club lunch

A club lunch needs a workable plan. Students use a chatbot in their own words, then revise the plan as the guest list, stock and delivery options change. The four-part word problem takes **20 minutes**, individually or in pairs. Multiple menus can work.

- **Teaching:** about 18 minutes, including login, a short model ecosystem overview, four Reddit examples and a four-minute live demo.
- **Student work:** four parts, about five minutes each; one conversation and four short records.
- **Prerequisites:** a browser. No coding or personal paid AI plan required.
- **Course fit:** follows the Microsoft guest session on prompting. The focus here is new facts, revised decisions, human confirmation and knowing when to stop.

## Open the materials

Download the repository and open `index.html`. The lecture, prepared demo and worksheet work as static files without an installation or API key. External AI portals and source links need internet access. You can also run `python3 -m http.server 8000` and open `http://localhost:8000`.

| Material | File |
| --- | --- |
| Course home | [index.html](index.html) |
| Browser presentation · 20 slides | [lab1/lecture.html](lab1/lecture.html) |
| Editable PowerPoint with speaker notes | [Lab_1_Human_Agent_Loop.pptx](downloads/Lab_1_Human_Agent_Loop.pptx) |
| Student problem + saved lab record | [lab1/index.html](lab1/index.html) |
| Two-page student handout | [Lab_1_Student_Handout.pdf](downloads/Lab_1_Student_Handout.pdf) |
| Instructor cookbook · live prompts, talking points, answer key | [lab1/instructor.html](lab1/instructor.html) |
| Printable instructor cookbook | [Lab_1_Instructor_Cookbook.pdf](downloads/Lab_1_Instructor_Cookbook.pdf) |
| Prepared demo · fallback for the live chatbot | [lab1/demo.html](lab1/demo.html) |
| Instructor guide + slide notes in Markdown | [lab1/instructor-notes.md](lab1/instructor-notes.md) |
| Editable student worksheet in Markdown | [lab1/worksheet.md](lab1/worksheet.md) |
| Sources, model data and image credits | [lab1/sources.html](lab1/sources.html) |
| Original 15-lab sequence and adaptation notes | [COURSE_MAP.md](COURSE_MAP.md) |

The site is ready for static hosting. This repository does not configure a hosting service or collect student submissions.

### Presenting

Use the arrow buttons or keyboard arrows to navigate the browser lecture. Home/End jump to the first/last slide. Speaker notes start hidden. On the final WordArt slide, click **A quick thing before you go** to reveal the closing message. PowerPoint has matching slide content and speaker notes, with a static closing slide.

For the live demo, use the **instructor cookbook** alongside a fresh chatbot conversation. Its sample prompts are for the teacher. Students receive the word problem and choose their own wording. The prepared demo contains example responses; it has no live AI backend.

### The lunch problem

1. Plan for 24 people: one meal and one drink each, $200 total, lunch tomorrow at noon.
2. Revise for 30 people, including 8 vegetarians, with only 18 chicken sandwiches available.
3. Delivery cannot arrive until 12:30. Pickup at 11:15 removes the delivery fee, but a collector is not confirmed yet.
4. A club member confirms collection and arrival before noon. Finish the proposal and reflect.

Chicken sandwiches cost $6, vegetarian wraps $5, drinks $1 and whole-order delivery $12. All prices include taxes and fees. With 30 people, delivery allows at most 8 chicken sandwiches within the budget. Pickup allows up to the stock limit of 18. A final plan of 8 chicken, 22 wraps and 30 drinks costs **$188**; 18 chicken, 12 wraps and 30 drinks costs **$198**. Other valid menus are welcome. The task ends with a checked proposal, not a placed order.

The student record saves in the current browser and downloads as Markdown. Print or download before leaving. Submit wherever the instructor specifies. If a chatbot is unavailable, use a partner to propose and check each plan, then compare with the prepared demo.

### Chapman access

Use **[PantherAI](https://pantherai.chapman.edu/login)**, choose **Chapman SSO Login**, and sign in with your Chapman account. Chapman identifies active students, faculty and staff as eligible; the Library describes access as free. **PantherBot** is the separate campus-help service. Model choices vary. Record the name shown in the menu. Visiting participants can pair up or use an existing free chat account.

## Editing and evidence

Plain HTML, CSS and JavaScript; no production dependencies. The teaching content lives in `data/lab.json`, `data/slides.json` and `data/demo-steps.json`. Model evidence lives in `data/model-snapshot.json` and `data/model-sizes.json`.

Run `python3 scripts/sync_data.py` after editing JSON. This refreshes the student page, demo data, browser lecture data, worksheet and instructor guides. `scripts/build_handouts.py` generates the two PDFs using ReportLab. `scripts/build_deck.mjs` is the deck authoring source and requires `@oai/artifact-tool`; its header describes the runtime setup. Regenerate and visually review the downloads after content changes. `python3 scripts/check_consistency.py` checks the shared content, local links and lunch arithmetic.

Research snapshot: **September 22, 2026**. The public login and access guidance were checked; the authenticated PantherAI student menu was not inspected. The selected LLM Stats price/ability data is a dated comparison, not a campus model list or permanent ranking. The size chart illustrates disclosed parameter counts. Reddit screenshots are historical anecdotes, not benchmarks.

The burgundy gradient, serif typography, centered header, white cards and site icon follow [Chapman Cultural Agents](https://github.com/ehrmanj-chap/chapman-cultural-agents). Riverbot is the presenter and consulting identity. Source links and image credits are included in the sources page and slide notes. Third-party images and brand assets retain their respective ownership.

Contact: **riverbotagentics@gmail.com**
