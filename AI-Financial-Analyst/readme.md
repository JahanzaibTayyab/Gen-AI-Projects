# AI Financial Analyst Assistant with Assistants API

## Project Overview

### Introduction

This project involves building an AI Financial Analyst Assistant using the Assistants API. The Assistant will leverage the Financial Modeling Prep API to retrieve real-time financial data and provide insightful analysis based on user queries.

### Assistants API

The Assistants API empowers the Assistant with the ability to interpret code, retrieve information, and make function calls. In this project, we will specifically utilize function calling to describe financial functions and intelligently retrieve the necessary functions and their arguments.

### Financial Modeling Prep API

The Financial Modeling Prep API serves as the primary source for real-time financial data. It offers various endpoints for accessing financial information, including stock quotes, financial statements, ratios, and more.

API Documentation: [Financial Modeling Prep API](https://site.financialmodelingprep.com/developer/docs?ref=mlq.ai)

## Project Steps

### 1. Defining Financial Functions

Define the necessary Financial Modeling Prep API calls to retrieve relevant financial data. These functions will serve as the core components of our Assistant's analytical capabilities.

### 2. Defining the Assistant

Leverage models, tools, and knowledge within the Assistants API to create an intelligent Assistant. Utilize the function calling tool to enable the Assistant to intelligently return the financial functions that need to be called along with their arguments.

### 3. Creating a Thread

Establish a conversation flow, known as a Thread, where user queries, function call responses, and Assistant replies can be seamlessly managed.

### 4. Adding Messages

Input user queries into the Thread in the form of Messages. These queries will drive the Assistant's actions and responses.

### 5. Running the Assistant

Create a Run, which represents the Assistant processing the Thread. This involves calling necessary tools, making function calls, and generating appropriate responses to user queries.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/JahanzaibTayyab/Gen-AI-Projects/tree/main/AI-Financial-Analyst
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure API keys:

   Obtain API keys for the Financial Modeling Prep API and update the configuration file with the required credentials.

4. Run the Assistant:

   ```bash
   python main.py
   ```

## Contributions

Contributions to this project are welcome. If you have suggestions, improvements, or feature ideas, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the developers of the Assistants API and the Financial Modeling Prep API for providing the tools and data needed to create this AI Financial Analyst Assistant.

Happy coding!
