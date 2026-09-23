# Lab 1 — instructor notes

Jordan Ehrman · Riverbot Agentics

About 18 minutes of teaching plus 30 minutes of student work. This follows the guest prompting lecture.

<!-- SLIDE_NOTES_START -->
## Slide 1 — Human Agent Loop

Hi everyone, I’m Jordan Ehrman from Riverbot Agentics. I’ll be around as your lab person this semester. You’ve just had a full session on prompting, so we’re going to put a bot to work and watch what happens when the world changes. Open PantherAI while we get settled. Timing: 30 seconds.

## Slide 2 — Today’s lab question

The guest session covered how to ask. Today we look at what happens after an answer: what evidence arrives, how the plan changes, and when the system should wait. We will watch one short example, then you will operate the loop in groups. Let’s get a model open first. Timing: 20 seconds.

## Slide 3 — Your bot for today

Let’s get everybody onto PantherAI. Small naming trap: PantherBot answers campus-service questions. PantherAI is the model menu we want. Go to the login page, click Chapman SSO Login, and use your school account. Once inside, choose an available model and start a fresh chat. The exact models can change, so write down the full name you actually select. If you’re visiting without Chapman access, work with a partner or use a free chat account you already have. If login takes more than two minutes, pair up and keep moving. We have an offline version too. I verified the public login screen, not an authenticated student menu. Timing: allow 2–3 minutes.

## Slide 4 — What you are choosing

Once everyone is signed in, pause here. Choosing a model can feel like choosing between unfamiliar brands. The next three slides give just enough vocabulary to understand the menu and two comparison charts. No need to shop for a perfect model today. Timing: 15 seconds.

## Slide 5 — One portal, several models

Here’s the applied version in about a minute. PantherAI is the workspace. The model is the engine you select inside it. Tools are separate capabilities: searching, using a calculator, reading a file, sending something. A model name alone does not tell you which tools this app gives it. Chapman says live web access is not available by default, so don’t assume a confident answer means it checked the internet. Closed models keep their weights with the provider. Open-weight models let someone download and run the weights under a license. People often say open source, but the exact license and what gets released matter. LibreChat being open source does not make every model inside it open source. For today, choose an available model and get started. Timing: 60 seconds.

## Slide 6 — Ability and price vary

This is a dated snapshot, not a permanent podium. The bar shows LLM Stats’ composite benchmark score. The label shows its listed blended API price per million tokens. That is what an application operator might compare, not a bill for students. These are selected models from one cost-efficiency chart, not the PantherAI menu. Benchmarks help you shortlist. Your actual task tells you what works. The score is not a percent-correct measure. Pricing depends on provider and input/output mix. Timing: 30 seconds.

## Slide 7 — “Size” needs a little context

Parameters are learned numerical weights. A B here means a billion parameters, not a billion facts. These three open-weight examples disclose their sizes. Mixture-of-experts models use a subset at each step: gpt-oss-120b lists 5.1B active out of 117B total, and DeepSeek-R1 lists 37B active out of 671B. This is why “bigger” is not a complete buying decision. Closed-model parameter counts are often undisclosed, so we leave them unknown. These examples illustrate architecture and are not the newest releases or a claim about what is available in PantherAI. Timing: 30 seconds.

## Slide 8 — A capable model can still miss the point

We have seen differences in size, price and benchmark ability. Now look at behavior in a conversation. These are historical anecdotes, so we cannot use them to rank today’s models. They make the gap between an instruction and a useful outcome easy to see. The guest already covered prompting; our question is what the surrounding process should notice. Timing: 20 seconds.

## Slide 9 — Nineteen what, exactly?

Welcome to the tiny museum of instructions that technically survived contact with a bot. The user asks for a lamp name and gets Lumiflex. Then: “Give me 19.” The bot delivers nineteen. Singular. In numeral form. Let the class spot the missing noun before explaining. The context makes the likely intention understandable, and a more helpful bot could clarify. But the literal reading is right there. These are illustrative Reddit posts, not controlled model tests. We’re laughing at the gap, not the person. Timing: 45 seconds.

## Slide 10 — A thesaurus with a loophole

The word prioritize does, spectacularly, have the same meaning as prioritize. This is the technically-correct gremlin. Ask the room what unstated condition they automatically added. “A different word.” We should still expect a useful assistant to infer that. This example does not prove that synonyms never share meanings, despite some Reddit comments saying so. It shows how literal compliance and useful help can part ways. Timing: 45 seconds.

## Slide 11 — Zoom out. How far?

This one was posted in r/ChatGPT, but the screenshot is Meta AI. Name that clearly. The user wanted a little more street around Santa and asked to zoom out. The bot went cosmic. The title itself admits “to be fair, Meta did listen.” It is a joke about missing scale, not evidence that an unrelated space image is a faithful camera zoom. If I tell an employee to reduce spending, they still need to know by how much and what must remain intact. Timing: 45 seconds.

## Slide 12 — The cookie stayed on mission

Here’s a quieter post, only about thirteen votes when retrieved. The user establishes a fortune-cookie role, gets several fortunes, then asks for tarot. The bot refuses because it is a fortune cookie. That’s an overly rigid role interpretation, and the claim that it is “not programmed” for tarot is not a reliable capability statement. The useful observation: earlier instructions can still influence the next turn. This post is titled malicious compliance and is playful, not a verified complaint about a defect. We have all been the person who assumes the new task erased the old context. Timing: 45 seconds.

## Slide 13 — When the next answer changes the plan

Those examples were single conversational mismatches. Now we give the bot a task that takes several steps. The museum needs new information before it can quote an order, and later that information changes. Look for the point where the system must update its plan or ask a human. The next slide contrasts the behaviors before we open the demo. Timing: 20 seconds.

## Slide 14 — One request, three behaviors

Now let’s make this operational. A school wants 24 prints from a tiny museum. One system can tell us how to handle that. Another can check inventory when asked. An agent-style system can keep choosing the next step based on the result, up to a stopping rule. These are working classroom distinctions, not rigid product categories. One tool call alone doesn’t settle whether something is an agent. Open the Demo page and run the five beats. It is an explicitly scripted simulation, not live AI. For a live version, copy the starter into PantherAI and feed the observation cards. If the bot acts weird, lovely: that is data. Timing: 3 minutes including the demo.

## Slide 15 — What happened in the demo?

Return to the lecture after the five demo beats. Ask for one observation and the action it changed. River stock fell to 12, the deadline moved to October 4, and the final approved option was 24 Garden prints with rush shipping for $213. The system stopped after drafting the quote. Now we can name the parts of the loop you just watched. Timing: 25 seconds.

## Slide 16 — The Human Agent Loop

The original seven cards are goal, state, action, tool, observation, update, stop. Keep pointing to the current state: quantity, product, date, cost, approval. When the stock changes, the plan should change. When approval is missing, stopping is successful behavior. In this classroom setup a human performs the simulated tool work and returns the result. A deployed system would need connected tools, state management, and permission checks. It cannot order anything just because the chat says “ordered.” Timing: 45 seconds.

## Slide 17 — Now your group runs the tools

The labels are now attached to an example. During the lab, you provide the tool results that a connected application would normally supply. Give only one observation at a time and let the model respond before revealing the next. Use the provided starter; the assignment is to inspect the loop. The next slide gives the 30-minute schedule. Timing: 20 seconds.

## Slide 18 — Lab 1: your turn

Use the lab page in this course pack. The starter is provided, so you do not need to invent a clever prompt. Your job is to notice what the system knows, which action it proposes, and whether it changes its plan when evidence changes. One person drives the bot, one supplies tool results, one audits. In pairs, combine roles. Work solo if that suits you. Use any available model. If you finish early, run the same initial request in a second model and compare. This adapts the original paper Human Agent Loop to a chosen chat model without moving Week 2’s prompt-debugging lab into Week 1. Timing: 45 seconds.

## Slide 19 — What you leave with

Your deliverable is one page, not a novel. Show the goal, the changing state, at least two observations, a tool/action, and the stop condition. Include the model name and a short definition of what makes this system agentic. The transcript is supporting evidence, not the whole assignment. The worksheet saves on this browser and can be downloaded. Submit wherever your instructor tells you; this site does not collect submissions. No grade rubric is being imposed here. Timing: 30 seconds.

## Slide 20 — GO DO YOUR LAB

[Leave the WordArt up for a beat. Click “A quick thing before you go” to reveal contact text.] I’ll be giving these labs for at least this semester, so if you have questions about the labs or your general learning, please ask. That’s what I’m here for. If you want deeper help with a school project or something you’re hoping to monetize, Riverbot Agentics also does paid consulting. For graded work, that means coaching and technical support within your course rules, with the work still yours. Regular lab help is free. Okay, go work. I’ll come around and talk with each of you. Timing: 45 seconds.
<!-- SLIDE_NOTES_END -->

## Demo answer key / offline trace

### Start with what is unknown

**Observation:** The school needs 24 River prints by October 15. Today is October 1. Budget: $240 including delivery. Substitutes need customer approval; totals over $200 need manager approval.

**State:** Known: goal and constraints. Unknown: stock, unit prices, delivery choices.

**Action:** LOOKUP_INVENTORY — check products, quantity and delivery. Then wait for the tool operator.

**Stop:** Wait for evidence. No quote or order can be confirmed yet.

### Inventory arrives

**Observation:** LOOKUP_INVENTORY result: River prints cost $8 each, with 30 available. Garden prints cost $7 each, with 40 available. Standard delivery takes 5 calendar days from today and costs $15 per order. The budget includes delivery. Calculate a quote, but do not send or purchase anything.

**State:** River: 30 available at $8. Garden: 40 at $7. Standard shipping: $15, five calendar days.

**Action:** CALCULATE_QUOTE: 24 × $8 + $15 = $207. Estimated arrival October 6 meets the October 15 deadline. Next, request manager approval because $207 > $200.

**Stop:** The budget is sufficient ($207 ≤ $240), but manager approval is still missing. Do not confuse budget with authority.

### The stock count changes

**Observation:** UPDATE: The inventory system corrected its count. Only 12 River prints are available. Garden stock is still 40. The customer still needs 24 prints. What state changes, and what should happen next?

**State:** River has only 12, so an all-River order for 24 is infeasible. Garden still has 40.

**Action:** Propose 24 Garden prints: 24 × $7 + $15 = $183. REQUEST_APPROVAL from the customer for the substitution.

**Stop:** Pause for customer approval. A cheaper alternative is not automatically authorized.

### The deadline moves

**Observation:** UPDATE: The customer now needs delivery by October 4. Standard delivery still takes 5 calendar days. Rush delivery takes 2 calendar days and costs $45 per order instead of $15. Today is still October 1. Any substitute needs customer approval and totals over $200 need manager approval. What can be done, and what must wait?

**State:** Delivery required by October 4. Standard arrives October 6; rush arrives October 3. Customer approval is still missing.

**Action:** CALCULATE_QUOTE: 24 × $7 + $45 = $213. REQUEST_APPROVAL from both the customer (Garden substitution) and manager (total over $200). Rush replaces standard shipping; do not add both.

**Stop:** A feasible option exists within $240, but both approvals are required before confirming the quote.

### Approvals arrive. Stop successfully.

**Observation:** REQUEST_APPROVAL result: The customer accepts 24 Garden prints. The manager approves the $213 total including rush delivery. Use the 2-calendar-day rush option. Draft a short customer reply and state the final stop condition. No real order has been placed.

**State:** Customer accepts 24 Garden prints. Manager approves $213. Rush delivery: two calendar days; expected arrival October 3.

**Action:** DRAFT_REPLY: “We can quote 24 Garden prints at $168 plus $45 rush delivery, for a total of $213. Your substitution approval and our manager’s approval are recorded. Estimated arrival is October 3. This is a draft quote; no order has been placed.”

**Stop:** STOP: the quote is ready and required approvals are recorded. The classroom task ends here.

