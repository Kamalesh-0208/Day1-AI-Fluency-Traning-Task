import json

from config import client, MODEL, banner
from tools import (
    get_course_fee,
    compare_course_fees,
    calculate_scholarship,
)


# --------------------------------------------------
# TOOLS AVAILABLE TO THE AI AGENT
# --------------------------------------------------

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Get the fee of a course.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string",
                        "description": "Course code such as CS101, AI202, or DS303"
                    }
                },
                "required": ["course_code"],
            },
        },
    },

    {
        "type": "function",
        "function": {
            "name": "compare_course_fees",
            "description": "Compare the fees of two courses.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course1": {
                        "type": "string"
                    },
                    "course2": {
                        "type": "string"
                    },
                },
                "required": ["course1", "course2"],
            },
        },
    },

    {
        "type": "function",
        "function": {
            "name": "calculate_scholarship",
            "description": "Calculate the total fee after applying a scholarship percentage.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course1": {
                        "type": "string"
                    },
                    "course2": {
                        "type": "string"
                    },
                    "scholarship_percent": {
                        "type": "number"
                    },
                },
                "required": [
                    "course1",
                    "course2",
                    "scholarship_percent",
                ],
            },
        },
    },
]


# --------------------------------------------------
# TOOL EXECUTION
# --------------------------------------------------

def run_tool(name, arguments):

    if name == "get_course_fee":

        return get_course_fee(
            arguments["course_code"]
        )

    elif name == "compare_course_fees":

        return compare_course_fees(
            arguments["course1"],
            arguments["course2"],
        )

    elif name == "calculate_scholarship":

        return calculate_scholarship(
            arguments["course1"],
            arguments["course2"],
            arguments["scholarship_percent"],
        )

    return {
        "error": "Unknown tool"
    }


# --------------------------------------------------
# AI AGENT
# --------------------------------------------------

def agent(question):

    messages = [

        {
            "role": "system",
            "content": (
                "You are a college fee assistant. "
                "Use the available tools whenever private "
                "course-fee information or calculations are required. "
                "All course fees are in Indian Rupees (₹). "
                "Always display fees using ₹, never $, USD, "
                "or any other currency. "
                "Do not invent course fees. "
                "Use the tools to obtain private course information."
            ),
        },

        {
            "role": "user",
            "content": question,
        },
    ]


    # Agent loop:
    # Reason → Act → Observe → Repeat / Finish

    while True:

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0,
        )

        message = response.choices[0].message


        # If the model does not request a tool,
        # it has finished the task.

        if not message.tool_calls:

            return message.content.strip()


        # Add the assistant's tool request
        # to the conversation.

        messages.append(message)


        # Execute every tool requested by the model.

        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name

            arguments = json.loads(
                tool_call.function.arguments
            )


            print(
                f"  [Agent selected tool: {tool_name}]"
            )


            # Python executes the selected tool.

            result = run_tool(
                tool_name,
                arguments
            )


            # Send the tool result back to the LLM.

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_name,
                    "content": json.dumps(result),
                }
            )


# --------------------------------------------------
# TEST THE AGENT
# --------------------------------------------------

if __name__ == "__main__":

    banner("SYSTEM 3: AI AGENT")


    questions = [

        "What is the fee for AI202?",

        "What is the total fee for CS101 and AI202 after a 10% scholarship?",

        "Is DS303 more expensive than CS101, and by how much?",

        "Write a two-line welcome message for new AI students.",

    ]


    for question in questions:

        print("Q:", question)

        print(
            "A:",
            agent(question)
        )

        print("-" * 70)