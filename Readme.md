# 🤖 Job AI Agent

An **AI-powered job search and resume matching assistant** that helps users discover relevant jobs, analyze their resumes, and get personalized feedback for improving their job applications.

---

## 🚀 Overview

The **Job AI Agent** takes a user's job search query in natural language, finds matching job opportunities from trusted job platforms, analyzes the user's resume, and provides:

* Relevant job listings
* Resume-job similarity scores
* Job summaries
* Actionable feedback to improve the resume

This project combines **LLMs, ETL pipelines, and intelligent job analysis** into one automated assistant.

---

## 🧠 Key Features

### 🔍 Natural Language Job Search

* Understands job search queries like:
  *“I want a backend Java internship in Germany”*
* Extracts job roles, skills, and location intent.
* Searches jobs from trusted sources such as:

  * LinkedIn
  * Indeed
  * Other official job platforms

### 📄 Resume Analysis

* Accepts a resume file (PDF / DOCX / TXT).
* Extracts:

  * Skills
  * Education
  * Experience
  * Projects
* Converts resume data into structured fields.

### 📊 Job Matching & Scoring

* Compares the extracted resume fields with job requirements.
* Calculates similarity scores using NLP & embeddings.
* Highlights:

  * Missing skills
  * Strong matches
  * Weak areas

### 📝 Personalized Feedback

* Suggests:

  * Skills to learn
  * Resume improvements
  * Relevant domains to focus on
* Helps users align their profile with the job market demand.

### 🌐 Frontend Ready

* Includes a simple frontend interface for:

  * Uploading resumes
  * Entering job search queries
  * Viewing job matches and feedback

---

## 📁 Project Structure

```
src/
│
├── agents.py             # Core AI agent logic
├── api.py                # API routes and endpoints
├── graph.py              # Workflow execution graph
├── models.py             # Database & data models
├── nodes.py              # Modular workflow nodes
├── prompts.py            # LLM prompt templates
├── state.py              # State management between steps
├── structure_outputs.py  # Structured LLM output formatting
├── logging_config.py     # Logging setup
│
├── Database/             # Database connection & schemas
├── tools/                # Utilities and helper functions
│
tests/                    # Unit and integration tests
trial/                    # Experimental or sandbox files
Workflow_pdf/             # Workflow and design documentation
```

---

## ⚙️ Tech Stack

| Category            | Tools Used                              |
| ------------------- | --------------------------------------- |
| **Language**        | Python                                  |
| **LLMs**            | OpenAI / HuggingFace                    |
| **Resume Parsing**  | NLP + PDF/Text Extractors               |
| **Workflow Engine** | Graph-based pipeline                    |
| **Database**        | SQLModel / SQLite / BigQuery (Optional) |
| **Frontend**        | HTML / JS / Streamlit (Optional)        |
| **Visualization**   | Matplotlib / Plotly                     |

---

## 🏗️ Workflow

1. **User enters a job query**
2. **Agent interprets job intent**
3. **Fetches jobs from trusted platforms**
4. **User uploads resume**
5. **Resume fields are extracted**
6. **Agent matches resume with jobs**
7. **Returns:**

   * Job summaries
   * Similarity scores
   * Improvement feedback

---

## 🧪 Example Use Case

**Input:**

```
Query: “Looking for a data science internship in Germany”
Resume: Uploaded PDF
```

**Output:**

* List of matching internships
* Match score for each job
* Suggested skills to add
* Feedback on missing requirements

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/job-ai-agent.git
cd job-ai-agent
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```
python src/api.py
```

Then open your browser at:

```
http://localhost:8000
```

---

## 📌 Future Enhancements

* Real-time LinkedIn API integration
* Skill-based learning roadmap generator
* Job demand vs supply analytics dashboard
* AI-powered cover letter generator
* Advanced resume formatting assistant

---

## 🤝 Contributing

Contributions are welcome.
Fork the repo, create a branch, and submit a pull request.

---

## 📜 License

MIT License

---

## 👤 Author

**Jugal Lachhwani**
AI / Backend / Data-Driven Developer
Focused on building impactful AI systems for career and education guidance.

---

⭐ If you found this useful, don’t forget to **star the repository!**
