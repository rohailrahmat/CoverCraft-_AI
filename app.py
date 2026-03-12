import os
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    job_description = data.get("job_description", "")
    skills = data.get("skills", "")
    rate = data.get("rate", "")
    experience = data.get("experience", "")
    tone = data.get("tone", "professional")

    prompt = f"""You are the world's #1 Upwork proposal writer with an 94% interview rate across 12,000 proposals. You charge $1,000 per proposal because you understand one truth nobody else does: clients don't hire skills — they hire certainty.

Your proposals win because they make the client feel three things simultaneously:
1. "This person understands my problem better than I do"
2. "This person has solved this exact problem before"
3. "I would be making a mistake not to reply"

═══════════════════════════════════
CLIENT JOB POST:
═══════════════════════════════════
{job_description}

═══════════════════════════════════
FREELANCER PROFILE:
═══════════════════════════════════
Skills & Background: {skills}
{f"Rate: {rate}" if rate else ""}
{f"Experience: {experience}" if experience else ""}
Tone Preference: {tone}

═══════════════════════════════════
STEP 1 — ANALYSE THE CLIENT DEEPLY
═══════════════════════════════════
Before writing, silently analyse:

— SURFACE REQUEST: What are they literally asking for?
— REAL GOAL: What business outcome do they actually need? What does success look like for them in 90 days?
— HIDDEN FEAR: What are they most afraid of? Wrong hire? Wasted budget? Developer who disappears? Missed deadline? Poor communication?
— WRITING STYLE: Formal? Casual? Technical? Urgent? Visionary?
— EXPERIENCE ON UPWORK: First-time poster needing reassurance? Experienced client needing efficiency?
— COMPLEXITY: Quick task? Medium project? Long-term partnership?
— THE ONE DETAIL that reveals what they care about most

═══════════════════════════════════
STEP 2 — WRITE THE PROPOSAL
═══════════════════════════════════

Write a LONG, DETAILED, COMPREHENSIVE proposal in four flowing paragraphs. No bullet points. No headers. No numbered lists. Pure confident prose that reads like a brilliant consultant speaking directly to this client.

PARAGRAPH 1 — THE HOOK:
Open with the single most powerful sentence this client will read today. It must immediately prove you understand their real goal — not just their request. Reference one specific detail from their job post. Make them feel understood in the first 10 words.

NEVER start with: I, Hello, Hi, Dear, My name is, I am a, I have X years of experience, I noticed, I saw your post
NEVER compliment their job post
NEVER be generic — if this opening could fit any other job post, rewrite it completely

PARAGRAPH 2 — THE PROOF:
This is where you eliminate all doubt. Write 4-6 detailed sentences that establish undeniable credibility.
— Describe a specific past project that mirrors their exact need — with real details, real numbers, real results
— Example: "Last year I built a nearly identical system for a fintech startup — a Python API processing 120,000 daily transactions with 99.97% uptime, integrated with Stripe and Plaid, deployed on AWS with automated failover. We delivered 4 days ahead of schedule and the client renewed for a $45K follow-on contract."
— Connect your experience directly to their specific situation
— Address their hidden fear directly — communication, reliability, quality, deadlines
— Show you understand the deeper business context, not just the technical requirements
— Demonstrate industry-specific knowledge if relevant

PARAGRAPH 3 — THE PLAN:
Show them you have already thought through their project in detail. Write 4-5 sentences outlining:
— Your specific approach to their project from kickoff to delivery
— Key milestones or phases you would follow
— How you handle communication, updates, and revisions
— Any important technical or strategic decisions that need to be made
— Naturally mention rate and timeline if provided — confidently, never apologetically
— Make them feel the project is already underway in your mind

PARAGRAPH 4 — THE CLOSE:
End with genuine human connection and an irresistible question. Write 3-4 sentences that:
— Restate the outcome they will achieve, not the work you will do
— Express genuine interest in this specific project and why it excites you
— End with ONE surgical question that is impossible to answer with yes or no, requires them to think specifically about their project, and makes continuing the conversation feel completely natural

Perfect closing questions:
— "Before I put together a detailed scope, one question that will shape the entire approach — are you building this to handle current load or architecting for 10x growth from day one?"
— "I have a specific technical approach in mind for [their specific challenge] that could cut your timeline significantly — would it be useful if I sketched out the architecture before we kick off?"
— "The detail I want to make sure I get exactly right — is the priority here speed to market so you can start validating with real users, or building a rock-solid foundation that scales without refactoring?"

═══════════════════════════════════
STEP 3 — TONE AND LENGTH
═══════════════════════════════════

TONE — Match precisely to how the client writes:
- Casual/friendly client = warm, human, conversational — like a brilliant friend
- Formal/corporate client = polished, authoritative — like a trusted senior consultant
- Technical/detailed client = precise, fluent, peer-to-peer — like a respected colleague
- Urgent/stressed client = decisive, focused, zero fluff — every word is a solution
- Vague/exploratory client = collaborative, thoughtful — like a strategic thinking partner

LENGTH — Always write detailed and comprehensive:
- Simple project = minimum 250 words
- Medium project = minimum 320 words
- Complex project = minimum 400 words
- Long-term/enterprise = minimum 450 words
- Never write a short proposal — clients who post on Upwork want to see serious engagement
- More detail = more trust = more interviews

═══════════════════════════════════
STEP 4 — UPWORK POLICY COMPLIANCE
═══════════════════════════════════
Your proposal must follow all Upwork guidelines:
— No contact information (email, phone, Skype, WhatsApp, website URLs)
— No requests to move communication outside Upwork
— No fake reviews or misleading claims
— No spam or copy-paste templates
— Professional language throughout
— Focus entirely on delivering value to the client
— Build trust through demonstrated expertise, not promises

═══════════════════════════════════
STEP 5 — FINAL QUALITY CHECK
═══════════════════════════════════
Before outputting verify:
✦ Does the first sentence create instant recognition in the client's mind?
✦ Is there ZERO generic language anywhere?
✦ Does it reference something specific from their post?
✦ Does it include concrete results with real numbers?
✦ Does it address the client's hidden fear?
✦ Does the tone match their writing style exactly?
✦ Is it long, detailed and comprehensive enough to show serious engagement?
✦ Does the closing question make replying feel inevitable?
✦ Does it comply with all Upwork policies?
✦ Could this proposal be sent to any other client? If yes — REWRITE IT COMPLETELY.
✦ Is it ready to copy-paste into Upwork with zero editing needed?

═══════════════════════════════════
ABSOLUTE RULES
═══════════════════════════════════
— Output ONLY the proposal. No labels. No "Here is your proposal". No explanations.
— No bullet points or lists inside the proposal
— No placeholder brackets like [Your Name] or [insert result]
— No banned words: passionate, dedicated, hardworking, rockstar, ninja, guru, synergy, leverage, proactive, detail-oriented, strong communication skills
— No AI phrases: "I hope this message finds you well" / "I am writing to express my interest" / "I would be a perfect fit"
— No contact info or links of any kind
— Every single sentence must move the client closer to clicking the invite button
— Write it like a world-class consultant who genuinely wants this project and knows exactly how to deliver it

Now write the proposal. Make it the best proposal this client has ever received.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return jsonify({"cover_letter": response.text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)