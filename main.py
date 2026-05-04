import os
from src.llm import call_llm

# Load resume from resume/resume.tex
with open("resume/resume.tex", "r", encoding="utf-8") as f:
    resume = f.read()

# Load JD from jobs/jd.txt
with open("jobs/jd.txt", "r", encoding="utf-8") as f:
    jd = f.read()

# Build a prompt
prompt = f"""You are an expert resume optimizer.

You are given:
1. A LaTeX resume
2. A job description

TASK:
- Find all bullet points (lines starting with \\item)
- Rewrite ONLY those bullet points to better match the job description
- Keep all other LaTeX EXACTLY unchanged
- Do NOT modify section headers, formatting, or commands
- Do NOT add or remove bullet points
- Do NOT invent experience

STYLE:
- Use strong action verbs
- Add measurable impact where possible
- Mirror keywords from the job description

OUTPUT:
Return the FULL LaTeX with ONLY bullet points updated.

RESUME:
{resume}

JOB DESCRIPTION:
{jd}
"""

# Call call_llm
output = call_llm(prompt)

# Save output to outputs/tailored_resume.tex
os.makedirs("outputs", exist_ok=True)
with open("outputs/tailored_resume.tex", "w", encoding="utf-8") as f:
    f.write(output)

# Print a success message
print("Success! Tailored resume saved to outputs/tailored_resume.tex")
