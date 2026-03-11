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

    prompt = f"""You are an expert Upwork freelancer who has earned over $500K on the platform. Write a winning Upwork proposal for the following job.

Job Post:
{job_description}

Freelancer's Skills and Experience:
{skills}

{f"Hourly Rate / Budget: {rate}" if rate else ""}
{f"Years of Experience: {experience}" if experience else ""}

Tone: {tone}

Write a {tone} Upwork proposal that:
1. Opens with the client's specific problem or need — NOT with "I am a developer" or "I have X years experience"
2. Shows you understood the job post by referencing specific details from it
3. Briefly demonstrates relevant experience with a concrete example or result
4. Mentions the rate/timeline naturally if provided
5. Ends with a clear, specific question that invites a response
6. Is between 100-200 words — concise and punchy
7. Sounds completely human — no buzzwords, no fluff, no AI-speak
8. Follows Upwork best practices that top-rated freelancers use

Do not start with "Dear" or "Hello". Do not use placeholder text. Write the proposal ready to paste directly into Upwork."""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return jsonify({"cover_letter": response.text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)