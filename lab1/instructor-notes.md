# Instructor cookbook — Plan the club lunch

Jordan Ehrman · Riverbot Agentics

About 18 minutes teaching + 20 minutes student work.

## Five-minute prep

- Open a fresh chatbot conversation and check the model name. Keep personal or student information out of the fictional example.
- Open the lecture, this cookbook, and the prepared demo in separate tabs. Have the student page or handout ready to share.
- Read the four turns once. The sample route costs $180, then $200, then $188 with pickup. Other menus can work.
- If login takes more than two minutes, pair students up. The prepared example and printable handout work without a live model.

## Run of show

- 0–3 minutes: Introduce yourself; students open a chatbot.
- 3–5 minutes: App, model and tools; the two comparison charts.
- 5–8 minutes: Four Reddit moments and quick audience reactions.
- 8–12 minutes: Live lunch demo: four turns; use the cookbook below.
- 12–18 minutes: Debrief, name the loop, explain the lab and give the closing invitation.
- 18–38 minutes: Students work through the four parts, about five minutes each.

## On-screen walkthrough

Use one fresh conversation. These sample messages are for the instructor; students use their own words. About one minute per part. If the model stalls, open the prepared demo. If it makes a mistake, inspect it together.

## Demo part 1 — Make a first plan

**Type or say:** I’m planning a fictional student club lunch tomorrow at noon for 24 people. Each needs one meal and one drink. Chicken sandwiches are $6, vegetarian wraps $5, drinks $1, and delivery is $12 for the entire order. All prices include taxes and fees; my total budget is $200. Help me propose an order and identify what I should check before committing. We are only planning.

**Say to the room:** We have enough information to make a provisional plan. We do not yet know everyone’s dietary needs, the stock, or whether delivery will arrive on time.

**Look for:** One possible starting plan is 24 chicken sandwiches, 24 drinks and delivery: 24 × $6 + 24 × $1 + $12 = $180. It fits the budget but still needs dietary, stock and timing checks. A mix of meals is equally valid.

**If it needs a nudge:** Which parts of that plan are confirmed, and which are assumptions? Show me the arithmetic.

## Demo part 2 — The guest list changes

**Type or say:** Update: there are now 30 people, including 8 vegetarians. The supplier has only 18 chicken sandwiches, but enough wraps and drinks. The $200 total budget and one meal plus one drink per person still apply. How should we revise the plan?

**Say to the room:** Eight vegetarians means at least eight wraps. It does not mean everyone else needs chicken. The stock limit and the budget are different constraints.

**Look for:** With delivery, 8 chicken sandwiches + 22 wraps + 30 drinks + $12 delivery = $48 + $110 + $30 + $12 = $200. All 30 wraps also work at $192. At most 8 chicken sandwiches fit the budget while delivery is included.

**If it needs a nudge:** Check the total including delivery. Does every person get a meal and a drink, with at least eight vegetarian meals?

## Demo part 3 — Delivery falls through

**Type or say:** The earliest delivery is 12:30 p.m., but lunch starts at noon. We can pick up at 11:15 a.m. with no delivery fee. A club member might collect it, but has not confirmed. What can we plan now, and what must wait?

**Say to the room:** A cheaper order is useful, but it does not get the food to the event. “Might collect” is not a confirmed pickup.

**Look for:** Pickup could solve the timing problem, but the collector and arrival before noon are still unconfirmed. Keeping 8 chicken, 22 wraps and 30 drinks costs $188 with pickup. Changing to 18 chicken, 12 wraps and 30 drinks costs $198. Either is a provisional option; there is no need to spend all $200.

**If it needs a nudge:** What evidence do we need before we call pickup a confirmed plan? What should we do if the member cannot collect it?

## Demo part 4 — Close the loop

**Type or say:** The club member confirms pickup at 11:15 a.m. and arrival at the lunch before noon. Give me a short final proposal with quantities, total cost and collection details. Explain why our planning task is complete. No order has been placed.

**Say to the room:** We can stop because the proposal meets the constraints and the pickup is confirmed. Finishing a plan is different from placing an order.

**Look for:** Example final proposal: 8 chicken sandwiches, 22 vegetarian wraps and 30 drinks, total $188. The confirmed club member collects at 11:15 a.m. and brings the order before noon. This serves 30 people, covers 8 vegetarians, uses no more than 18 chicken sandwiches and stays within $200. Planning is complete; ordering is a separate action.

**If it needs a nudge:** Point to the evidence for the quantity, dietary requirement, stock, budget and arrival time.

## Answer key

For C chicken sandwiches, Part 1 costs $156 + C (0–24 chicken). Part 2 costs $192 + C (0–8 chicken). Pickup in Parts 3–4 costs $180 + C (0–18 chicken). Other meals are wraps. Pickup removes the delivery fee; the menu may stay the same.

- **Serves everyone:** 30 meals and 30 drinks.
- **Meets dietary needs:** At least 8 vegetarian wraps; more are allowed.
- **Respects stock:** No more than 18 chicken sandwiches.
- **Fits the budget:** No more than $200 including any delivery fee.
- **Arrives on time:** Confirmed 11:15 a.m. pickup and arrival before noon.
- **Stops at the right point:** A checked proposal, with no claim that an order was placed.

At five-minute intervals, invite students to the next part. Ask which facts carried forward and what is still an assumption. Accept different menus that meet all constraints. No prescribed prompt, diagram or transcript is required.


# Slide-by-slide speaker notes

## Slide 1 — Human Agent Loop

Hi everyone, I’m Jordan Ehrman from Riverbot Agentics. I’ll be around as your lab person this semester. You’ve just had a session on prompting, so today we will use a bot and watch what happens when the facts change. Our very ambitious mission: get lunch to a student club. Open PantherAI while we get settled. Timing: 30 seconds.

## Slide 2 — Today’s lab question

The guest session covered how to ask. Today we look at what happens after an answer: what information arrives, how the plan changes, and when a person needs to step in. This is a chatbot exercise that makes the human part of an agent loop visible. Timing: 20 seconds.

## Slide 3 — Your bot for today

Let’s get everybody onto PantherAI. Small naming trap: PantherBot answers campus-service questions. PantherAI is the model menu we want. Go to the login page, click Chapman SSO Login, and use your school account. Once inside, choose an available model and start a fresh chat. The exact models can change, so write down the full name you actually select. If you’re visiting without Chapman access, work with a partner or use a free chat account you already have. If login takes more than two minutes, pair up and keep moving. We have an offline version too. I verified the public login screen, not an authenticated student menu. Timing: allow 2–3 minutes.

Sources:
- https://www.chapman.edu/campus-services/information-systems/research-technology-support/pantherai/index.aspx
- https://pantherai.chapman.edu/login
- https://libguides.chapman.edu/AI/approved_tools

## Slide 4 — What you are choosing

Once everyone is signed in, pause here. Choosing a model can feel like choosing between unfamiliar brands. The next three slides give just enough vocabulary to understand the menu and two comparison charts. No need to shop for a perfect model today. Timing: 15 seconds.

## Slide 5 — One portal, several models

Here’s the applied version in about a minute. PantherAI is the workspace. The model is the engine you select inside it. Tools are separate capabilities: searching, using a calculator, reading a file, sending something. A model name alone does not tell you which tools this app gives it. Chapman says live web access is not available by default, so don’t assume a confident answer means it checked the internet. Closed models keep their weights with the provider. Open-weight models let someone download and run the weights under a license. People often say open source, but the exact license and what gets released matter. LibreChat being open source does not make every model inside it open source. For today, choose an available model and get started. Timing: 60 seconds.

Sources:
- https://www.chapman.edu/campus-services/information-systems/research-technology-support/pantherai/index.aspx
- https://www.librechat.ai/
- https://opensource.org/ai/open-source-ai-definition

## Slide 6 — Ability and price vary

This is a dated snapshot, not a permanent podium. The bar shows LLM Stats’ composite benchmark score. The label shows its listed blended API price per million tokens. That is what an application operator might compare, not a bill for students. These are selected models from one cost-efficiency chart, not the PantherAI menu. Benchmarks help you shortlist. Your actual task tells you what works. The score is not a percent-correct measure. Pricing depends on provider and input/output mix. Timing: 30 seconds.

Sources:
- https://llm-stats.com/models/qwen3-32b
- https://llm-stats.com/methodology/llm-stats-score

## Slide 7 — “Size” needs a little context

Parameters are learned numerical weights. A B here means a billion parameters, not a billion facts. These three open-weight examples disclose their sizes. Mixture-of-experts models use a subset at each step: gpt-oss-120b lists 5.1B active out of 117B total, and DeepSeek-R1 lists 37B active out of 671B. This is why “bigger” is not a complete buying decision. Closed-model parameter counts are often undisclosed, so we leave them unknown. These examples illustrate architecture and are not the newest releases or a claim about what is available in PantherAI. Timing: 30 seconds.

Sources:
- https://huggingface.co/Qwen/Qwen3-32B
- https://huggingface.co/openai/gpt-oss-120b
- https://huggingface.co/deepseek-ai/DeepSeek-R1

## Slide 8 — A capable model can still miss the point

We have seen differences in size, price and benchmark ability. Now look at behavior in a conversation. These are historical anecdotes, so we cannot use them to rank today’s models. They make the gap between an instruction and a useful outcome easy to see. The guest already covered prompting; our question is what the surrounding process should notice. Timing: 20 seconds.

## Slide 9 — Nineteen what, exactly?

Welcome to a few instructions that technically survived contact with a bot. The user asks for a lamp name and gets Lumiflex. Then: “Give me 19.” The bot delivers nineteen. Singular. In numeral form. Let the class spot the missing noun before explaining. The context makes the likely intention understandable, and a more helpful bot could clarify. But the literal reading is right there. These are illustrative Reddit posts, not controlled model tests. We’re laughing at the gap, not the person. Timing: 45 seconds.

Sources:
- https://www.reddit.com/r/ChatGPT/comments/1hgx336/19/

## Slide 10 — A thesaurus with a loophole

The word prioritize does, spectacularly, have the same meaning as prioritize. This is the technically-correct gremlin. Ask the room what unstated condition they automatically added. “A different word.” We should still expect a useful assistant to infer that. This example does not prove that synonyms never share meanings, despite some Reddit comments saying so. It shows how literal compliance and useful help can part ways. Timing: 45 seconds.

Sources:
- https://www.reddit.com/r/ChatGPT/comments/1anff5w/incredible/

## Slide 11 — Zoom out. How far?

This one was posted in r/ChatGPT, but the screenshot is Meta AI. Name that clearly. The user wanted a little more street around Santa and asked to zoom out. The bot went cosmic. The title itself admits “to be fair, Meta did listen.” It is a joke about missing scale, not evidence that an unrelated space image is a faithful camera zoom. If I tell an employee to reduce spending, they still need to know by how much and what must remain intact. Timing: 45 seconds.

Sources:
- https://www.reddit.com/r/ChatGPT/comments/1hofvi0/when_i_said_zoom_out_please_i_was_wanting_to_see/

## Slide 12 — The cookie stayed on mission

Here’s a quieter post, only about thirteen votes when retrieved. The user establishes a fortune-cookie role, gets several fortunes, then asks for tarot. The bot refuses because it is a fortune cookie. That’s an overly rigid role interpretation, and the claim that it is “not programmed” for tarot is not a reliable capability statement. The useful observation: earlier instructions can still influence the next turn. This post is titled malicious compliance and is playful, not a verified complaint about a defect. We have all been the person who assumes the new task erased the old context. Timing: 45 seconds.

Sources:
- https://www.reddit.com/r/ChatGPT/comments/zgivfv/be_a_fortune_cookie_malicious_compliance/

## Slide 13 — Now let the world change

The jokes show gaps between a request and a useful response. Now let’s watch the same conversation meet changing facts. The goal stays simple: one meal and one drink for everyone, within budget, ready for noon. Timing: 20 seconds.

## Slide 14 — One lunch, a few moving parts

Open the instructor cookbook beside a fresh chatbot conversation. Run its four sample turns in about four minutes, pausing once after the pickup uncertainty. Use the prepared demo if login or the model stalls. Do not demand an exact response: a mistake is a useful discussion point. This exercise simulates parts of an agent loop with a person supplying facts; the chatbot is not independently checking stock, contacting anyone or ordering lunch. Timing: 4 minutes including the demo.

Sources:
- Original Beginner_Agentics_15_Week_Demo_Lab_Guide.docx, Week 1 (Aug 10, 2026)
- https://www.anthropic.com/engineering/building-effective-agents

## Slide 15 — What changed the plan?

Ask for one new fact and the decision it changed. In our sample, 8 chicken, 22 wraps and 30 drinks cost $200 with delivery, then $188 with pickup. Keeping that menu is valid; 18 chicken and 12 wraps for $198 is also valid after pickup is confirmed. Do not imply there is one required menu. Timing: 30 seconds.

## Slide 16 — The Human Agent Loop

These are names for what you just did, not labels students must paste into every prompt. The original loop also names tools and observations: a real system could use an inventory lookup, calculator or messaging tool, then observe the result. Today the human supplies the facts and checks the arithmetic. At Part 3, waiting is appropriate. At Part 4, the planning task can end. A chatbot conversation alone does not show that a real-world action happened. Timing: 45 seconds.

Sources:
- Original Beginner_Agentics_15_Week_Demo_Lab_Guide.docx, Week 1
- https://www.anthropic.com/engineering/building-effective-agents

## Slide 17 — Your conversation. Your decisions.

There is no prescribed starter and no special command language. Students choose what to tell the bot, what to ask, and which answer to challenge. In a pair, one can type while the other checks; switch halfway. Show the student lab page, not the instructor answer key. Timing: 20 seconds.

## Slide 18 — Four parts. Twenty minutes.

Read each part when you reach it. Spend about five minutes per part. Write a few sentences about the plan and what changed. Multiple meal mixes can work. The point is to keep the constraints straight and know when you have enough evidence to finish. Students can work individually or in pairs using any available chatbot. Timing: 30 seconds.

Sources:
- Original Beginner_Agentics_15_Week_Demo_Lab_Guide.docx, Week 1
- Original AI_Agents_Course_Syllabus (1).pdf, Week 1

## Slide 19 — Leave with a plan you can defend

A few sentences per part are enough. Students can type into the lab page or use the printable handout. Download browser work before leaving; submit wherever your instructor specifies. The page does not collect submissions. A surprising failure counts if the student explains the correction. No loop diagram or full transcript is required. Timing: 30 seconds.

Sources:
- Original Beginner_Agentics_15_Week_Demo_Lab_Guide.docx, Week 1

## Slide 20 — GO DO YOUR LAB

[Leave the WordArt up for a beat. Click “A quick thing before you go” to reveal contact text.] I’ll be giving these labs for at least this semester, so if you have questions about the labs or your general learning, please ask. That’s what I’m here for. If you want deeper help with a school project or something you’re hoping to monetize, Riverbot Agentics also does paid consulting. For graded work, that means coaching and technical support within your course rules, with the work still yours. Regular lab help is free. Okay, go work. I’ll come around and talk with each of you. Timing: 45 seconds.

Sources:
- https://github.com/ehrmanj-chap/riverbot-agentics
