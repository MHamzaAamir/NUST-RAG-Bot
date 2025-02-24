# NUST Student Handbook RAG System

This project is a Retrieval-Augmented Generation (RAG) system designed to answer student queries using the NUST student handbook. The system retrieves relevant passages from the handbook, formulates a prompt, and generates responses using a language model.

## Features
- Embeddings are generated from the student handbook.
- A Python script (`nust_query_app.py`) provides a GUI-based interface for student queries.
- The system retrieves the most relevant content based on cosine similarity.
- Queries are answered using the Gemini AI model.

## Setup Instructions
### 1. Install Dependencies
Ensure you have Python installed along with the required libraries:
```bash
pip install pandas google-generativeai scikit-learn tkinter
```

### 2. Generate Embeddings
Run the provided Jupyter Notebook (`test.ipynb`) to process the student handbook and store embeddings. The embeddings are saved in a `.pkl` file.

### 3. Run the Query App
Execute the Python script to launch the GUI-based application:
```bash
python nust_query_app.py
```

## File Descriptions
- `test.ipynb`: Processes the student handbook and generates embeddings.
- `nust_query_app.py`: Provides a graphical interface for students to input queries and receive answers.
- `embeddings.pkl`: Stores precomputed embeddings for quick retrieval.

## How It Works
1. **Embedding Generation:** The Jupyter Notebook generates text embeddings from the NUST handbook.
2. **Query Processing:** When a student inputs a query, the system computes its embedding.
3. **Retrieval:** The system finds the most relevant passages based on cosine similarity.
4. **Response Generation:** The retrieved passages are fed into a prompt for the Gemini AI model to generate a response.
5. **GUI Interface:** The system provides a simple Tkinter-based user interface for students to interact with.

## Example Usage
1. Open the GUI by running `nust_query_app.py`.
2. Enter a query, e.g., "What is the attendance policy?".
3. Click the send button to receive an AI-generated response.

## Notes
- Ensure your API key for Gemini AI is correctly configured in `nust_query_app.py`.
- The system may not answer questions outside the handbook's scope accurately.

## Future Improvements
- Expand the dataset beyond the handbook.
- Improve retrieval accuracy with better embedding techniques.
- Enhance the UI for a better user experience.

