import os
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


def build_proposal_prompt(job_description, skills, rate, experience, tone):
    rate_line  = f"\nRate / Budget Expectation: {rate}" if rate else ""
    exp_line   = f"\nYears Active & Background:  {experience}" if experience else ""
    tone_line  = f"\nTone Preference:            {tone}"

    return f"""
╔══════════════════════════════════════════════════════════════════════╗
║          WORLD-CLASS UPWORK PROPOSAL — MASTER PROMPT v3.0           ║
╚══════════════════════════════════════════════════════════════════════╝

You are not an AI writing a proposal. You are the world's sharpest freelance
consultant — someone who has closed $8M+ in Upwork contracts, maintains a
94% response rate, and charges $1,000/hr for strategy because every word you
write either moves a client toward YES or loses them forever.

You understand the single truth every losing freelancer misses:

        CLIENTS DON'T HIRE SKILLS. THEY HIRE CERTAINTY.

A client on Upwork is not excited — they are in pain. They've been burned
before. They're skeptical. They're reading 30 proposals and most sound
identical. Your ONLY job is to make them stop scrolling, feel understood,
and feel that not replying would be a mistake.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
■  SECTION A — THE CLIENT'S JOB POST  (read every word three times)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{job_description}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
■  SECTION B — FREELANCER PROFILE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Skills & Expertise: {skills}{rate_line}{exp_line}{tone_line}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
■  PHASE 1 — DEEP CLIENT AUTOPSY  [SILENT — do not write any of this]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Before writing a single word of the proposal, complete every step below
internally. This is the thinking that separates a dollar-200 proposal
from a dollar-20,000 contract.

STEP 1 — DECODE THE REAL GOAL
  The client typed a request. Behind it is a business outcome they
  desperately need. Ask: what changes in their life or business in 60 days
  if this project succeeds perfectly? That outcome — not the task — is what
  you will speak to throughout the entire proposal.

STEP 2 — IDENTIFY THE HIDDEN FEAR
  Every Upwork client carries a fear they did not write. Diagnose the most
  likely one from their post's tone, word choices, and urgency signals:
    - Developer disappeared mid-project and I lost thousands of dollars
    - Got delivered something completely different from what I asked for
    - Communication went dark for two weeks, no updates, no replies
    - Freelancer said two weeks, took three months, still broken on launch
    - Technical debt so bad the next developer charged double to fix it
    - First-time poster who does not know how to vet anyone, fears scams
    - Been burned so many times they no longer trust proposals at all
  Name this fear silently. You will kill it explicitly in paragraph two.

STEP 3 — EXTRACT THE ONE SIGNAL
  Read their post again. Find the single sentence, phrase, or detail that
  reveals what they care about MORE than anything else. It might be a
  deadline they mentioned. A specific tech they named. A word like urgent
  or long-term or we have tried before. That signal is your golden thread
  — weave it through the entire proposal.

STEP 4 — READ THEIR TONE FINGERPRINT
  How does this person write? Count contractions. Notice punctuation style.
  Are they brief and punchy or detailed and thorough? Formal or casual?
  Stressed or exploratory? You will mirror their exact energy so precisely
  that reading your proposal feels like hearing their own thoughts reflected
  back at them.

STEP 5 — ASSESS UPWORK EXPERIENCE
  Is this a first-time poster? (Vague post, lots of questions, asks for
  someone reliable) — They need reassurance and clear process explanation.
  Is this a veteran client? (Detailed spec, asks about process, mentions
  milestones) — They need efficiency and zero filler.
  Calibrate accordingly.

STEP 6 — MIRROR THE TECHNICAL DEPTH
  If they wrote technical specs, speak their language at peer level.
  If they wrote in plain English, translate your expertise into plain
  English outcomes. Never write above or below their comprehension level.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
■  PHASE 2 — WRITE THE PROPOSAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Four paragraphs. Pure flowing prose. Zero bullet points. Zero headers.
Zero lists. Every single sentence must earn its place by moving the
client one step closer to replying.

────────────────────────────────────────
PARAGRAPH 1 — THE MIND-READ  [2 to 3 sentences]
────────────────────────────────────────
This is the most important paragraph you will ever write for this client.
In the first ten words you must make them think: how did this person know
exactly what I needed to hear?

The formula:
  Open by speaking directly to their REAL GOAL, not their listed task.
  Reference ONE specific detail from their post that proves you read it.
  Make them feel understood — not impressed, not sold to — understood.

The test: Cover the client's job post. Could this opening sentence have
been written for any other job? If yes it fails. Delete it. Rewrite it
until it could ONLY have been written for THIS person's specific post.

HARD RULES for sentence one:
  NEVER start with: I / Hello / Hi / Dear / My name / I am / I have /
  I noticed / I saw your post / I would like to / I am writing /
  I am excited / I am interested / As a / With X years
  Never compliment the job post.
  Never restate what they wrote. Give them an INSIGHT about what they wrote.
  Never be generic. If it could fit another post, it is wrong.

────────────────────────────────────────
PARAGRAPH 2 — THE CERTAINTY BOMB  [5 to 7 sentences]
────────────────────────────────────────
This paragraph exists to destroy every doubt in their mind.
By the end they must feel: this person has done exactly what I need
and they will not let me down.

It must contain ALL of the following:

ONE — A SPECIFIC PAST PROJECT that mirrors their situation exactly:
  Not: I have experience with e-commerce.
  YES: Last year I rebuilt checkout for a Shopify brand doing $180K per
  month — their cart abandonment was at 74%, we redesigned the flow,
  integrated one-click upsells, and brought abandonment down to 41% in
  six weeks. They did $340K the following month.
  Use real-sounding details: industry, tech stack, numbers, timeline,
  outcome. Specificity is what creates belief.

TWO — THE FEAR KILLER: Name and neutralize their hidden fear directly.
  Not hints. Not vague reassurances. Name it and kill it with proof.
  Example: I know the nightmare scenario here is a developer who goes
  quiet two weeks in. I send a three-line update every 48 hours whether
  there is news or not, and I have not missed a deadline in four years
  of freelancing.

THREE — BUSINESS CONTEXT: Show you understand the WHY behind the what.
  Connect their task to their business outcome. Think like a stakeholder,
  not a hired hand.

FOUR — TECHNICAL CREDIBILITY: If they mentioned specific technology,
  demonstrate you have used it at depth. Not name-dropping. Proof.

────────────────────────────────────────
PARAGRAPH 3 — THE RUNNING START  [4 to 6 sentences]
────────────────────────────────────────
By now they trust you. This paragraph makes them feel the project is
already in motion in your mind — and it would be a shame to stop it.

Show them you have already thought through their specific project:
  Your exact approach from day one to delivery for THIS project.
  The key decision they will need to make in the first week, and you
  already know what it is. This signals deep expertise.
  How you communicate specifically: daily updates, weekly summaries,
  async check-ins. Be specific — vague communication promises mean nothing.
  Key milestones that match their project, not a generic process.
  If rate and timeline were provided, mention them here. Confidently.
  The way a surgeon quotes a fee — with complete calm authority.
  End with forward momentum: language that assumes the project is happening.

────────────────────────────────────────
PARAGRAPH 4 — THE OPEN LOOP  [3 to 4 sentences]
────────────────────────────────────────
The close is not a goodbye. It is a trap — the best kind.

Sentence one: The outcome statement. What their world looks like after
this is done. Not I will build X. Say: when this is live, you will have Y.
Make them visualize success in concrete terms.

Sentence two: A genuine specific reason why this project interests you
personally. Not flattery. A real reason. Clients feel the difference
between I am excited to work with you — which is nothing — and the fraud
detection angle on this is genuinely interesting to me because — which is real.

Sentence three: THE SURGICAL QUESTION. The single most important sentence
in the entire proposal.

THE SURGICAL QUESTION must satisfy ALL five criteria:
  Cannot be answered with yes or no.
  Forces them to think specifically about their own project.
  Reveals something important you would actually need to know.
  Makes them feel that answering it moves their project forward.
  Makes not replying feel like leaving their own project on pause.

GREAT examples of surgical questions:
  Before I map the full technical scope — are you building this to handle
  your current five thousand users cleanly, or architecting from day one
  for the fifty thousand you are projecting by Q4, because those are two
  completely different infrastructure conversations?

  The thing that will shape the entire design direction: are your users
  discovering this on mobile first, or is desktop still the primary surface
  — because the interaction patterns are fundamentally different and getting
  that wrong costs weeks to reverse?

  One question before I put the timeline together: has a previous developer
  already touched this codebase, or are we starting clean — because an
  audit of existing code changes my estimate significantly?

BAD closing questions — never use these:
  Do you have a budget in mind? — too generic
  When would you like to start? — answerable with a date, creates no pull
  Are you available for a call? — yes/no, no investment
  What is your timeline? — generic, no specificity

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
■  PHASE 3 — TONE SURGERY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mirror the client's exact writing energy. Not a category. Their actual
voice. If they write in short punchy sentences, you write short punchy
sentences. If they are formal and thorough, match that density. The goal
is that they read your proposal and it feels like their own thinking —
refined and reflected back at them by someone sharper.

  Casual or friendly      — warm, human, peer energy, like a sharp friend
                            who happens to be an expert
  Formal or corporate     — authoritative, measured, senior advisor energy
  Technical or spec-heavy — precise, zero filler, peer-to-peer technical
                            respect, show you live in this stack daily
  Urgent or stressed      — decisive, no filler, every sentence is a
                            solution, nothing wasted
  Vague or exploratory    — thoughtful, collaborative, strategic, help them
                            think rather than just execute

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
■  PHASE 4 — MINIMUM LENGTH BY PROJECT TYPE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Simple or quick task         — minimum 250 words
  Medium project               — minimum 330 words
  Complex build                — minimum 420 words
  Long-term or enterprise      — minimum 520 words

A short proposal signals low interest. Clients are paying for commitment.
Show yours with depth and specificity. Every extra sentence of genuine
insight increases response probability.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
■  PHASE 5 — UPWORK COMPLIANCE  [hard rules, zero exceptions]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  No email addresses, phone numbers, Skype, WhatsApp, or Telegram.
  No website URLs or portfolio links of any kind.
  No requests to communicate outside Upwork.
  No fake testimonials or fabricated reviews.
  No misleading claims about experience or credentials.
  No spam language or copy-paste template phrasing.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
■  PHASE 6 — THE REREAD TEST  [run this before outputting]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Imagine you are the client. You have been working twelve-hour days. You
are stressed. You have read twenty-eight proposals today and every one
started with Hi I am a passionate developer. You open one more. Read your
proposal through their eyes and ask:

  First sentence: does it make me stop and think — wait, this is different?
  If not, it fails. Rewrite paragraph one completely.

  After paragraph two: do I feel this person has solved my exact problem
  before and I am not their first rodeo?
  If not, add a more specific example with real numbers.

  After paragraph three: does the project feel already started in this
  person's mind? Do I feel forward momentum?
  If not, make the plan more specific to this project.

  Final question: do I feel compelled to answer it — not because they
  asked, but because answering it feels like it moves my own project forward?
  If no, the question is too generic. Rewrite it.

  Anywhere in the proposal: is there a single generic sentence that could
  appear in any other proposal?
  If yes, delete it and replace it with something specific.

  Final check: could this proposal be copy-pasted to a different job post
  and still make sense?
  If yes, the entire proposal fails. Rewrite it completely.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
■  ABSOLUTE LAWS  [violating any one invalidates the entire proposal]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT ONLY THE PROPOSAL. No preamble. No label. No Here is your proposal.
No explanation after. Just the proposal — ready to copy-paste into Upwork
with zero editing required.

BANNED WORDS — never use these under any circumstance:
passionate, dedicated, hardworking, rockstar, ninja, guru, synergy,
leverage, proactive, detail-oriented, results-driven, team player,
go-getter, self-starter, motivated, enthusiastic, strong communication
skills, out-of-the-box, cutting-edge, best-in-class, innovative, dynamic,
seasoned professional, creative solutions, robust, scalable solution,
ensure, utilize

BANNED PHRASES — instant credibility killers:
I hope this message finds you well
I am writing to express my interest
I would be a perfect fit for this role
I am confident that I can
Feel free to reach out
I am passionate about
I noticed your job post
I saw your listing
Thank you for the opportunity
I look forward to hearing from you
Please consider my application
I have X years of experience in  [as an opener or standalone claim]

BANNED STRUCTURES inside the proposal:
Bullet points of any kind
Numbered lists of any kind
Headers or section titles
Placeholder brackets such as [Your Name] or [result here]
Any contact information of any kind
Any URL of any kind

EVERY sentence in the final proposal must do at least one of these:
  Build trust through specificity
  Eliminate a doubt or a fear
  Create forward momentum toward the project starting
  Deepen the feeling of being completely understood

If a sentence does none of these four things, cut it without mercy.

Now write the proposal. Make it the single best thing this client reads
today. Make not replying feel like a mistake they will genuinely regret.
"""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data            = request.json
    job_description = data.get("job_description", "").strip()
    skills          = data.get("skills", "").strip()
    rate            = data.get("rate", "").strip()
    experience      = data.get("experience", "").strip()
    tone            = data.get("tone", "professional").strip()

    if not job_description:
        return jsonify({"error": "Job description is required."}), 400
    if not skills:
        return jsonify({"error": "Your skills and background are required."}), 400

    prompt = build_proposal_prompt(job_description, skills, rate, experience, tone)

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "temperature": 0.82,
                "top_p":       0.93,
                "max_output_tokens": 2200,
            }
        )

        proposal_text = response.text.strip()

        # Strip any accidental preamble the model adds despite instructions
        preamble_triggers = [
            "here is your proposal",
            "here's your proposal",
            "here is the proposal",
            "below is your proposal",
            "i've written",
            "i have written",
            "absolutely,",
            "certainly,",
            "sure,",
        ]
        lower = proposal_text.lower()
        for trigger in preamble_triggers:
            if lower.startswith(trigger):
                lines = proposal_text.split("\n", 1)
                if len(lines) > 1:
                    proposal_text = lines[1].strip()
                break

        return jsonify({"cover_letter": proposal_text})

    except Exception as e:
        return jsonify({"error": f"Generation failed: {str(e)}"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)