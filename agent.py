import os
import json
from dotenv import load_dotenv
from groq import Groq

from tools import (
    check_equipment,
    get_booking_details,
    calculate_late_fine
)

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# Tools available to the AI agent
tools = [
    {
        "type": "function",
        "function": {
            "name": "check_equipment",
            "description": "Check the availability of college lab equipment using private college data.",
            "parameters": {
                "type": "object",
                "properties": {
                    "equipment_name": {
                        "type": "string",
                        "description": "Name of the equipment"
                    }
                },
                "required": ["equipment_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_booking_details",
            "description": "Get private equipment booking details for a student.",
            "parameters": {
                "type": "object",
                "properties": {
                    "student_id": {
                        "type": "string",
                        "description": "Student ID such as S101"
                    }
                },
                "required": ["student_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_late_fine",
            "description": "Calculate the fine for returning equipment late.",
            "parameters": {
                "type": "object",
                "properties": {
                    "hours_late": {
                        "type": "integer",
                        "description": "Number of hours the equipment is returned late"
                    }
                },
                "required": ["hours_late"]
            }
        }
    }
]


# Execute the tool selected by the LLM
def execute_tool(tool_name, arguments):

    if tool_name == "check_equipment":
        return check_equipment(arguments["equipment_name"])

    elif tool_name == "get_booking_details":
        return get_booking_details(arguments["student_id"])

    elif tool_name == "calculate_late_fine":
        return calculate_late_fine(arguments["hours_late"])

    return {"error": "Unknown tool"}


# User question
user_question = input("Ask the AI agent: ")


messages = [
    {
        "role": "system",
        "content": """
You are an AI agent for a private college laboratory.

You have access to private equipment and student booking tools.

Never invent private college information.

Use the available tools whenever private information is required.

You may use more than one tool if the question requires multiple
pieces of information.

After receiving the tool results, provide a clear final answer.

Available student IDs for testing:
S101 = Oviya
S102 = Arun
"""
    },
    {
        "role": "user",
        "content": user_question
    }
]


# AI Agent Loop
while True:

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        tools=tools,
        tool_choice="auto",
        temperature=0
    )

    assistant_message = response.choices[0].message

    # Add the LLM response to the conversation
    messages.append(assistant_message)

    # If no tool is requested, the agent has completed the task
    if not assistant_message.tool_calls:

        print("\nAI Agent:")
        print(assistant_message.content)

        break

    # Execute every tool selected by the LLM
    for tool_call in assistant_message.tool_calls:

        tool_name = tool_call.function.name

        arguments = json.loads(
            tool_call.function.arguments
        )

        print(f"\n[Agent selected tool: {tool_name}]")
        print(f"[Arguments: {arguments}]")

        result = execute_tool(
            tool_name,
            arguments
        )

        print(f"[Tool result: {result}]")

        # Send the tool result back to the LLM
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            }
        )