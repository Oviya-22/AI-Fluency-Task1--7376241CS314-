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

### Example Request

```text
Ask the chatbot: Is the 3D Printer available?
```

The chatbot responds without accessing the private college database.

---

## 4. System 2 – Rule-Based Workflow

The rule-based workflow does not use an LLM.

It uses predefined conditions and rules to identify the request and execute the appropriate function.

### Rules

- Equipment name → Check equipment availability
- Student ID → Retrieve booking details
- Late hours → Calculate fine

**File:** `workflow.py`

### Example Requests

```text
Is the 3D Printer available?
Show booking details for S101
What is the fine for 2 hours late?
```

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
```

**File:** `agent.py`

### Example Request

```text
Ask the AI agent: Is the 3D Printer available?
```

The agent identifies the required tool, retrieves the private data, and generates a response using the tool result.

---

## 6. Project Structure

```text
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
```

---

## 7. Technologies Used

- Python
- Groq API
- OpenAI-compatible tool calling
- python-dotenv
- Rule-based programming
- Function-based tools
- Agent loop

---

## 8. Installation

### Step 1 – Install Dependencies

Run the following command:

```bash
python -m pip install -r requirements.txt
```

### Step 2 – Configure the API Key

Create a `.env` file in the project folder:

```text
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

The API key is stored locally and should not be uploaded to GitHub.

The `.gitignore` file prevents `.env` from being committed.

---

## 9. Running the Project

### 9.1 Plain Chatbot

Run:

```bash
python chatbot.py
```

Example:

```text
Ask the chatbot: Is the 3D Printer available?
```

The chatbot does not have access to the private college database.

---

### 9.2 Rule-Based Workflow

Run:

```bash
python workflow.py
```

The workflow uses predefined rules to process the test questions.

---

### 9.3 AI Agent

Run:

```bash
python agent.py
```

Example:

```text
Ask the AI agent: Is the 3D Printer available?
```

The terminal displays:

1. Selected tool
2. Tool arguments
3. Tool result
4. Final agent response

---

## 10. Output

Screenshots of all three systems are stored in the `Output` folder.

```text
Output/
├── chatbot_output.png
├── workflow_output.png
└── agent_output.png
```

These screenshots provide execution evidence for the three approaches.

### Output Screenshots

- `chatbot_output.png` – Plain chatbot execution
- `workflow_output.png` – Rule-based workflow execution
- `agent_output.png` – AI agent execution

---

## 11. Analysis

A detailed comparison of the three approaches is provided in:

```text
analysis.md
```

The analysis covers:

- Flexibility
- Decision-making
- Tool usage
- Private-data access
- Multi-step task handling
- Automation
- Reliability
- Suitability for the scenario

---

## 12. Objective

The objective of this project is to demonstrate the difference between:

- A plain LLM chatbot
- A deterministic rule-based workflow
- An AI agent that can use tools

The project shows how the three approaches handle the same private-data scenario using different mechanisms.

---

## 13. Comparison

| Feature | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| LLM Usage | Yes | No | Yes |
| Private Data Access | No | Yes | Yes |
| Tool Usage | No | Yes | Yes |
| Decision Making | LLM response | Predefined rules | LLM-based tool selection |
| Flexibility | Natural-language interaction | Limited to predefined rules | Handles varied requests |
| Multi-Step Tasks | Limited | Predefined | Can perform multiple tool calls |
| Automation | Conversational | Rule-driven | Tool-driven |
| Reliability | Depends on model response | Deterministic rules | Depends on model and tools |

---

## 14. Key Learning

This project demonstrates the progression from a simple LLM-based chatbot to a rule-based system and finally to an AI agent.

The plain chatbot can understand natural-language requests but does not have access to the private college data.

The rule-based workflow can access the private data through predefined rules, but its behavior depends on the conditions programmed by the developer.

The AI agent combines an LLM with tools, allowing it to understand requests, select tools, retrieve private information, and generate responses based on the tool results.

---

## 15. Files Description

| File | Purpose |
|---|---|
| `chatbot.py` | Implements the plain LLM chatbot |
| `workflow.py` | Implements the rule-based workflow |
| `tools.py` | Contains private data and reusable tools |
| `agent.py` | Implements the AI agent and tool-calling loop |
| `analysis.md` | Contains detailed comparison and suitability analysis |
| `requirements.txt` | Contains required Python packages |
| `.gitignore` | Prevents sensitive and unnecessary files from being committed |
| `README.md` | Project documentation |
| `Output/` | Contains screenshots of system execution |

---

## 16. Conclusion

The project demonstrates three different approaches to the same private college laboratory equipment scenario.

The comparison shows how access to private data, predefined rules, tools, and LLM-based interaction changes the way a system handles user requests.

The detailed evaluation of flexibility, decision-making, tool usage, private-data access, multi-step handling, automation, reliability, and suitability is available in `analysis.md`.