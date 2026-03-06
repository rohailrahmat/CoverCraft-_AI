import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from google import genai

load_dotenv()

app = Flask(__name__)

client = genai.Client(api_key=os.environ.get("AIzaSyBMGNrLURoJAzMmIClnAKYa1wtcxoJqar4"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    job_description = data.get("job_description", "")
    skills = data.get("skills", "")

    prompt = f"""Write a professional, compelling cover letter for someone applying for the following job.

Job Description:
{job_description}

Applicant's Skills and Experience:
{skills}

Write a complete, ready-to-send cover letter. Make it sound human, confident and professional. Do not use placeholder text like [Your Name] - just write the body of the letter starting from 'Dear Hiring Manager'."""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return jsonify({"cover_letter": response.text})

if __name__ == "__main__":
    app.run(debug=True)