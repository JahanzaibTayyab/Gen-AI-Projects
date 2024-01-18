# %% [markdown]
# # Step 0: Setting up the Environment

# %%
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import json
import requests
import time

_: bool = load_dotenv(find_dotenv())  # read local .env file
client: OpenAI = OpenAI()


# %% [markdown]
# # Step 1: Defining Financial Functions
#

# %%
FMP_API_KEY = os.environ["FMP_API_KEY"]


# %%
# Define financial statement functions
def get_income_statement(ticker, period, limit):
    url = f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?period={period}&limit={limit}&apikey={FMP_API_KEY}"
    response = requests.get(url)
    return json.dumps(response.json())


def get_balance_sheet(ticker, period, limit):
    url = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement-as-reported/{ticker}?period={period}&limit={limit}&apikey={FMP_API_KEY}"
    response = requests.get(url)
    return json.dumps(response.json())


def get_cash_flow_statement(ticker, period, limit):
    url = f"https://financialmodelingprep.com/api/v3/cash-flow-statement-as-reported/{ticker}?period={period}&limit={limit}&apikey={FMP_API_KEY}"
    response = requests.get(url)
    return json.dumps(response.json())


def get_financial_full_statement(ticker, period, limit):
    url = f"https://financialmodelingprep.com/api/v3/financial-statement-full-as-reported/{ticker}?period={period}&limit={limit}&apikey={FMP_API_KEY}"
    response = requests.get(url)
    return json.dumps(response.json())


def get_key_metrics(ticker, period, limit):
    url = f"https://financialmodelingprep.com/api/v3/key-metrics/{ticker}?period={period}&limit={limit}&apikey={FMP_API_KEY}"
    response = requests.get(url)
    return json.dumps(response.json())


def get_financial_ratios(ticker, period, limit):
    url = f"https://financialmodelingprep.com/api/v3/ratio/{ticker}?period={period}&limit={limit}&apikey={FMP_API_KEY}"
    response = requests.get(url)
    return json.dumps(response.json())


def get_financial_growth(ticker, period, limit):
    url = f"https://financialmodelingprep.com/api/v3/cash-flow-statement-growth/{ticker}?period={period}&limit={limit}&apikey={FMP_API_KEY}"
    response = requests.get(url)
    return json.dumps(response.json())


# %% [markdown]
# # Step 2: Map available functions
#

# %%
# Map available functions
available_functions = {
    "get_income_statement": get_income_statement,
    "get_balance_sheet": get_balance_sheet,
    "get_cash_flow_statement": get_cash_flow_statement,
    "get_financial_full_statement": get_financial_full_statement,
    "get_key_metrics": get_key_metrics,
    "get_financial_ratios": get_cash_flow_statement,
    "get_financial_growth": get_financial_ratios,
}


# %% [markdown]
# # Step 3: Creating the Assistant
#

# %%
from openai.types.beta import Assistant


def run_assistant(user_message):
    assistant: Assistant = client.beta.assistants.create(
        instructions="Act as a financial analyst by accessing financial data through the Financial Modeling Prep API. Your capabilities include analyzing key metrics, comprehensive financial statements, vital financial ratios, and tracking financial growth trends",
        model="gpt-3.5-turbo-1106",
        tools=[
            {"type": "code_interpreter"},
            {
                "type": "function",
                "function": {
                    "name": "get_income_statement",
                    "description": "FMP's Income Statement API provides access to real-time income statement data for a wide range of companies, including public companies, private companies, and ETFs. This data can be used to track a company's profitability over time, to compare a company to its competitors, and to identify trends in a company's business.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "ticker": {"type": "string"},
                            "period": {"type": "string"},
                            "limit": {"type": "integer"},
                        },
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_balance_sheet",
                    "description": "The balance sheet is a financial statement that displays a company’s total assets, liabilities, and shareholder equity over a specific timeframe (quarterly or yearly). Investors can use this statement to determine if the company can fund its operations, meet its debt obligations, and pay a dividend.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "ticker": {"type": "string"},
                            "period": {"type": "string"},
                            "limit": {"type": "integer"},
                        },
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_cash_flow_statement",
                    "description": "The cash flow statement is a financial statement that highlights how cash moves through the company, including both cash inflows and outflows.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "ticker": {"type": "string"},
                            "period": {"type": "string"},
                            "limit": {"type": "integer"},
                        },
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_financial_full_statement",
                    "description": "FMP's Full Financial Statement As Reported API provides access to all three of the financial statements (income statement, balance sheet, and cash flow statement) for a company as reported by the company. This data can be used to get a complete overview of a company's financial performance and health.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "ticker": {"type": "string"},
                            "period": {"type": "string"},
                            "limit": {"type": "integer"},
                        },
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_key_metrics",
                    "description": "Get key financial metrics for a company, including revenue, net income, earnings per share (EPS), and price-to-earnings ratio (P/E ratio). Assess a company's financial performance and compare it to its competitors.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "ticker": {"type": "string"},
                            "period": {"type": "string"},
                            "limit": {"type": "integer"},
                        },
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_financial_ratios",
                    "description": "Get financial ratios for a company, such as the P/B ratio and the ROE. Assess a company's financial health and compare it to its competitors.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "ticker": {"type": "string"},
                            "period": {"type": "string"},
                            "limit": {"type": "integer"},
                        },
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_financial_growth",
                    "description": "Get the cash flow growth rate for a company. Measure how quickly a company's cash flow is growing.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "ticker": {"type": "string"},
                            "period": {"type": "string"},
                            "limit": {"type": "integer"},
                        },
                    },
                },
            },
        ],
    )
    # Creating a new thread
    thread = client.beta.threads.create()
    # Adding a user message to the thread
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=user_message
    )
    # Running the assistant on the created thread
    run = client.beta.threads.runs.create(
        thread_id=thread.id, assistant_id=assistant.id
    )
    # Loop until the run completes or requires action
    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

        # Add run steps retrieval here
        run_steps = client.beta.threads.runs.steps.list(
            thread_id=thread.id, run_id=run.id
        )
        print("Run Steps:", run_steps)

        if run.status == "requires_action":
            tool_calls = run.required_action.submit_tool_outputs.tool_calls
            tool_outputs = []

            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)

                if function_name in available_functions:
                    function_to_call = available_functions[function_name]
                    output = function_to_call(**function_args)
                    tool_outputs.append(
                        {
                            "tool_call_id": tool_call.id,
                            "output": output,
                        }
                    )

            # Submit tool outputs and update the run
            client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread.id, run_id=run.id, tool_outputs=tool_outputs
            )

        elif run.status == "completed":
            # List the messages to get the response
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            for message in messages.data:
                role_label = "User" if message.role == "user" else "Assistant"
                message_content = message.content[0].text.value
                print(f"{role_label}: {message_content}\n")
                # Check the type of message content and handle accordingly
                for content in message.content:
                    if content.type == "text":
                        message_content = content.text.value
                        print(f"{role_label}: {message_content}\n")
                    elif content.type == "image_file":
                        # Handle image file content, e.g., print the file ID or download the image
                        image_file_id = content.image_file.file_id
                        # Define a path to save the image
                        image_save_path = f"./image_{image_file_id}.png"
                        # Download and save the image
                        download_and_save_image(image_file_id, image_save_path)
            break  # Exit the loop after processing the completed run

        elif run.status == "failed":
            print("Run failed.")
            break

        elif run.status in ["in_progress", "queued"]:
            print(f"Run is {run.status}. Waiting...")
            time.sleep(5)  # Wait for 5 seconds before checking again

        else:
            print(f"Unexpected status: {run.status}")
            break


# %%
run_assistant(
    "Can you compare the financial health of Microsoft and Apple over the last four years, focusing on their balance sheets and key financial ratios?"
)


# %% [markdown]
# # Step 5: Enabling Code Interpreter
#

# %%
run_assistant(
    "Evaluate Microsoft vs. Googles's revenue & profitability growth over the past 4 quarters. Visualize the results with one or more charts"
)
