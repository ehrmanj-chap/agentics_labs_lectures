# Lab 1 revision handoff — September 23, 2026

The September 22 request for transitional slides and Chapman Cultural Agents branding did not land on main. This draft preserves the completed browser-side revision after the editing environment disconnected.

## Completed on this branch

- 20 browser slides: the original 14 plus six bridges.
- Georgia typography, burgundy gradient, centered course header, and site icon from ehrmanj-chap/chapman-cultural-agents at b073714acc3333424815f9a51ad56a4485179109.
- Riverbot retained as presenter/consulting identity.
- Instructor HTML and Markdown synchronized to the 20-slide sequence.
- Teaching estimate updated to 18 minutes; student lab remains 30 minutes.
- Demo notes corrected to five beats.

## Still required before merge

1. Finish and upload the matching PowerPoint to downloads/Lab_1_Human_Agent_Loop.pptx.
2. Verify browser interactions and layout in an available preview environment.
3. Remove the draft-status wording in README.md and this handoff when complete.

## PowerPoint checkpoint

A 20-slide PPTX was created with the presentation skill, rendered, and passed package, font, geometry and native-chart validation. Its final review showed clipped leading text in the explanatory text boxes on the thesaurus and fortune-cookie slides (new slide numbers 10 and 12). The XML still contains the full text. Recreate those body boxes with explicit left alignment/insets and inspect them again.

The last verified file was /workspace/scratch/26957ee304e1/build/final/Lab_1_Human_Agent_Loop.pptx. Local edits were in /workspace/scratch/26957ee304e1/agentics_labs_lectures. The environment went offline before the final text repair and upload, so these paths may not be recoverable.

PPTX authoring notes: import the original 14-slide deck; retain original charts, screenshots, WordArt and speaker notes; switch text fonts to Georgia; use the centered cover; insert the six transition slides at the positions in data/slides.json. Keep Riverbot’s logo on the closing slide. Import/export dropped embedded workbook relationships; restore the original ppt/slides/charts/ and ppt/embeddings/ parts, including their content types, preserving chart data and formulas. Charts belong on new slides 6 and 7.

## Validation already performed locally

- JavaScript syntax checks passed for lecture, lecture data, demo and worksheet scripts.
- All local HTML asset/navigation links resolved.
- All 20 PowerPoint slides were rendered and visually reviewed; two text repairs remain as above.
- Cloud browser could not reach the local preview. No end-to-end browser pass is claimed.
