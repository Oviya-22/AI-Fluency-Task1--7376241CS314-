# Agentic AI: Foundations and Open-Source Practice

## Task 1 – Chatbot vs Rule-Based Workflow vs AI Agent

### 1. Scenario

This project demonstrates three different approaches to solving a private college laboratory equipment problem:

1. Plain Chatbot
2. Rule-Based Workflow
3. AI Agent

The scenario uses private college data related to laboratory equipment, student bookings, and late-return fines.

---

## 2. Private Data

### Equipment Data

| ID | Equipment | Department | Status | Available Slots |
|---|---|---|---|---:|
| E101 | 3D Printer | CSE | Available | 2 |
| E102 | VR Headset | CSE | Available | 4 |
| E103 | Arduino Kit | ECE | Issued | 0 |
| E104 | Raspberry Pi | CSE | Available | 3 |

### Student Data

| Student ID | Name | Department | Current Booking |
|---|---|---|---|
| S101 | Oviya | CSE | None |
| S102 | Arun | CSE | E102 |

### Fine Rule

The late-return fine is:

**₹20 per hour**

---

## 3. System 1 – Plain Chatbot

The plain chatbot uses an LLM without access to the private college database.

It can understand natural-language questions, but it cannot retrieve actual private equipment availability or student booking information.

**File:** `chatbot.py`

---

## 4. System 2 – Rule-Based Workflow

The rule-based workflow does not use an LLM.

It uses predefined conditions and rules to identify the request and execute the appropriate function.

Examples:

- Equipment name → check equipment availability
- Student ID → retrieve booking details
- Late hours → calculate fine

**File:** `workflow.py`

---

## 5. System 3 – AI Agent

The AI agent combines an LLM with private-data tools.

It can:

- Understand natural-language requests
- Select an appropriate tool
- Pass arguments to the tool
- Receive the tool result
- Continue the interaction when additional tool use is required
- Generate a final response

### Available Tools

```text
check_equipment()
get_booking_details()
calculate_late_fine()
File: agent.py

6. Project Structure
AI-Fluency-Task1/
│
├── chatbot.py
├── workflow.py
├── tools.py
├── agent.py
├── requirements.txt
├── README.md
├── analysis.md
├── .gitignore
│
└── Output/
    ├── chatbot_output.png
    ├── workflow_output.png
    └── agent_output.png

7. Technologies Used
Python
Groq API
OpenAI-compatible tool calling
python-dotenv
Rule-based programming
Function-based tools
Agent loop

8. Installation

Install the required packages:

python -m pip install -r requirements.txt

Create a .env file in the project folder:

GROQ_API_KEY=YOUR_GROQ_API_KEY

The API key is stored locally and should not be uploaded to GitHub.

9. Running the Project
Plain Chatbot
python chatbot.py

Example:

Ask the chatbot: Is the 3D Printer available?
Rule-Based Workflow
python workflow.py

The workflow runs predefined test questions.

AI Agent
python agent.py

Example:

Ask the AI agent: Is the 3D Printer available?

The terminal displays the selected tool, its arguments, the tool result, and the final response.

10. Output

Screenshots of all three systems are stored in the Output folder:

Output/
├── chatbot_output.png
├── workflow_output.png
└── agent_output.png

11. Analysis

A detailed comparison of the three approaches is provided in:

analysis.md

The analysis covers:

Flexibility
Decision-making
Tool usage
Private-data access
Multi-step task handling
Automation
Reliability
Suitability for the scenario

12. Objective

The objective of this project is to demonstrate the difference between a plain LLM chatbot, a deterministic rule-based workflow, and an AI agent that can use tools to interact with private data.
