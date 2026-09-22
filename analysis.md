# Day 1 Task: Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Scenario

For this task, I selected a private college laboratory equipment booking scenario. The system contains private information about laboratory equipment, student bookings, and late-return fines. The purpose is to demonstrate how the same problem can be handled using a plain chatbot, a rule-based workflow, and an AI agent.

The private equipment data contains four laboratory resources: a 3D Printer, a VR Headset, an Arduino Kit, and a Raspberry Pi. Each equipment record contains its equipment ID, department, availability status, and available slots. The system also contains private student booking information for students such as S101 and S102. In addition, the system uses a predefined fine rule of ₹20 for every hour an equipment item is returned late.

For example, the private data records the 3D Printer as E101 and currently available, while the Arduino Kit is recorded as issued. Student S101 has no current equipment booking, while student S102 currently has the VR Headset booked.

The same types of requests are tested with all three approaches. Examples include checking whether the 3D Printer is available, retrieving the booking details of a student, and calculating the fine for returning equipment late.

---

## 2. Plain Chatbot

The first approach is a plain chatbot. It uses a Large Language Model to generate responses to the user's questions. The chatbot does not have access to the private laboratory equipment database, student booking records, or fine-calculation functions. Therefore, it cannot reliably provide private information such as the actual availability of the 3D Printer or the equipment currently booked by a particular student.

The chatbot receives a user question and sends it to the language model. The language model then generates a response based on the information available to it. No external tools are provided to the model, so the chatbot cannot query the private data.

For example, when asked whether the 3D Printer is available, the chatbot cannot verify the actual status in the private college database. However, it can answer general questions such as explaining what a 3D printer is or how 3D printers are commonly used in educational laboratories.

The main limitation of the plain chatbot in this scenario is its lack of private-data access. It can produce natural-language responses, but it cannot directly retrieve or calculate information from the college's private system.

---

## 3. Rule-Based Workflow

The second approach is a rule-based workflow. Unlike the plain chatbot, this system directly accesses the private laboratory data through predefined Python functions. However, it does not use an LLM.

The workflow contains explicit conditions for recognizing supported requests. For example, if a question contains terms related to the 3D Printer and availability, the workflow calls the `check_equipment()` function for the 3D Printer. Similarly, questions containing a supported student ID can trigger the `get_booking_details()` function, and questions about supported late-return periods can trigger the `calculate_late_fine()` function.

The workflow therefore follows a fixed sequence of predefined rules. The program identifies a matching condition, executes the corresponding function, obtains the private data or calculation result, and returns the result to the user.

This approach is reliable for questions that match the rules implemented in the program. However, its flexibility is limited. A new equipment name, a different way of asking a question, or a new type of request may require additional rules to be manually programmed.

The rule-based workflow therefore demonstrates that private data can be accessed without an LLM, but the decision-making process is controlled entirely by predefined conditions.

---

## 4. AI Agent

The third approach is an AI agent. This system combines an LLM, tools, and an agent loop. The LLM receives the user's request and decides whether one or more tools are required to answer it.

Three tools are available to the agent. The `check_equipment()` tool checks private equipment information, the `get_booking_details()` tool retrieves private student booking information, and the `calculate_late_fine()` tool calculates the fine for a specified number of late hours.

When a user asks a question, the LLM analyzes the request and can select the appropriate tool. The selected tool is then executed by the Python program. The result is returned to the LLM as a tool message. The LLM observes the result and determines whether another tool is required or whether it can provide the final response.

This creates the agent loop:

**User Request → LLM → Tool Selection → Tool Execution → Tool Result → LLM Observation → Final Answer or Another Tool**

For example, a question asking whether the 3D Printer is available and what the fine would be for returning it two hours late can require more than one tool. The agent can call `check_equipment()` to obtain the equipment status and `calculate_late_fine()` to calculate the fine. It can then combine the results into a single final response.

The main advantage of the AI agent in this scenario is that the LLM can interpret a wider variety of natural-language requests and select the required tools dynamically. Its limitation is that the quality of the final response depends on correct tool selection and correct tool execution. The available tools and private data must also be designed carefully.

---

## 5. Comparison Table

| Basis for comparison | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Flexibility | Flexible for general conversation, but cannot access the private laboratory data | Limited to predefined rules and supported patterns | Can interpret natural-language requests and dynamically select available tools |
| Decision-making | LLM generates a response but has no private-data tools | Decisions are controlled by predefined conditions | LLM decides which available tool or tools are needed |
| Tool usage | No external tools | Uses predefined Python functions | Uses tools selected by the LLM |
| Private-data access | No access to the private equipment and booking database | Direct access through programmed functions | Accesses private data through tools |
| Multi-step task handling | Limited because no private tools are available | Requires explicitly programmed steps | Can use multiple tools in an agent loop |
| Automation | Automates response generation | Automates predefined processes | Automates dynamic tool selection and multi-step processing |
| Reliability | Cannot verify private data | Predictable for cases covered by its rules | Depends on correct tool selection, tool results, and LLM behavior |

---

## 6. Suitability Analysis

For this private laboratory equipment scenario, the AI agent is the most suitable approach when the system needs to handle different natural-language requests and combine information from multiple private tools. The agent can use the equipment availability tool, student booking tool, and fine calculation tool according to the requirements of the user's request.

The plain chatbot is useful when the task mainly requires general conversation or general explanations and does not require access to private college information. It is simple because no external tools or private database connections are required, but it cannot reliably answer questions that depend on the private laboratory records.

The rule-based workflow is suitable when the requests are predictable and the required actions can be clearly defined in advance. It can access private data and provide deterministic results for supported cases. However, adding new types of questions or handling different natural-language expressions requires additional rules.

The AI agent provides a combination of natural-language understanding and programmatic tool access. In this scenario, this allows the system to handle requests involving private equipment data, student booking information, and calculations while selecting the required tools dynamically. Therefore, for a laboratory assistant that needs to handle varied and potentially multi-step requests, the AI agent provides the required combination of flexibility, private-data access, tool usage, and multi-step task handling.

---

## 7. Conclusion

The three approaches are useful for different types of problems. A plain chatbot is appropriate when the main requirement is natural-language conversation, explanation, or general information and no private external data is required.

A rule-based workflow is appropriate when the process is predictable and the required decisions can be represented using fixed rules and conditions. It is useful when deterministic behavior is important and the possible inputs and actions are well defined.

An AI agent is appropriate when a task requires natural-language understanding together with access to external tools or private data and may involve multiple steps. The combination of an LLM, tools, and a loop allows the agent to interpret a request, select appropriate tools, observe their results, and continue processing until it can provide a final response.

This comparison demonstrates the main difference between the three approaches: a plain chatbot primarily generates responses using an LLM, a rule-based workflow follows predefined conditions, and an AI agent combines an LLM with tools and a loop to perform more dynamic multi-step tasks.