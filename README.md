# NUST Student Handbook RAG System

This project is a Retrieval-Augmented Generation (RAG) system designed to answer student queries using the NUST student handbook. The system retrieves relevant passages from the handbook, formulates a prompt, and generates responses using a language model.

## Features

- Embeddings are generated from the student handbook.
- A Python script (`nust_query_app.py`) provides a GUI-based interface for student queries.
- The system retrieves the most relevant content based on cosine similarity.
- Queries are answered using the Gemini 1.5 Flash Model.

## Setup Instructions

### 1. Install Dependencies

Ensure you have Python installed along with the required libraries:

```bash
pip install pandas google-generativeai scikit-learn tkinter python-dotenv
```

### 2. Set Up Environment Variables

To keep your API key secure, store it in a `.env` file instead of hardcoding it in the script.

1. Create a `.env` file in the project directory and add the following:

```
GENAI_API_KEY=your_api_key_here
```

### 3. Run the Query App

Execute the Python script to launch the GUI-based application:

```bash
python nust_query_app.py
```

## File Descriptions

- `test.ipynb`: Processes the student handbook and generates embeddings which are exported as .pkl file.
- `nust_query_app.py`: Provides a graphical interface for students to input queries and receive answers.
- `embeddings.pkl`: Stores precomputed embeddings for quick retrieval.
- `.env`: Stores environment variables (not included in version control).

## Example Usage

1. Open the GUI by running `nust_query_app.py`.
2. Enter a query, e.g., "What is the attendance policy in class?".
3. Click the send button to receive an AI-generated response.

## Notes

- Ensure your API key for Gemini AI is correctly configured in the `.env` file.
- The system may not answer questions outside the handbook's scope accurately.