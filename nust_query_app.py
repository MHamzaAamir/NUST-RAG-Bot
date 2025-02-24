import pandas as pd
import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext
from sklearn.metrics.pairwise import cosine_distances

genai.configure(api_key="AIzaSyC4K40iwfMXj9d-rUxXbX5h7xI8m0IPo98")
df = pd.read_pickle("embeddings")

def get_embeddings(text):
    model = 'models/text-embedding-004'
    embedding = genai.embed_content(model=model,
                                    content=text,
                                    task_type="retrieval_document")
    return embedding['embedding']


def get_relevant_docs(user_query):
    query_embeddings = get_embeddings(user_query) 
    def calculate_distance(embedding):
        return cosine_distances([query_embeddings], [embedding])[0][0]   
    df['dist'] = df['embeddings'].apply(calculate_distance)    
    top_docs = df.nsmallest(7, 'dist')    
    relevant_docs = top_docs['page_content'].tolist()
    return relevant_docs

def make_rag_prompt(query, relevant_passage):
    relevant_passage = ' '.join(relevant_passage)
    prompt = (
        f"Just give me the answer donot state that you are quoting it from the provided text"
        f"If the data has no relevant information then just say you dont know the answer. If is a general question then answer according to your intuition\n\n"
        f"QUESTION: '{query}'\n"
        f"relevant data: '{relevant_passage}'\n\n"
        f"ANSWER:"
    )
    return prompt

def generate_response(user_prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    answer = model.generate_content(user_prompt)
    return answer.text

def generate_answer(query):
    relevant_text = get_relevant_docs(query)
    prompt = make_rag_prompt(query, relevant_passage=relevant_text)
    answer = generate_response(prompt)
    return answer

def create_app():
    root = tk.Tk()
    root.title("NUST Query Interface")

    tk.Label(root, text="Enter your query:").pack(pady=5)
    prompt_box = tk.Entry(root, width=50)
    prompt_box.pack(pady=5)

    tk.Label(root, text="Response:").pack(pady=5)
    response_box = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD)
    response_box.pack(pady=5)

    def on_send():
        query = prompt_box.get()
        response = generate_answer(query)
        response_box.delete(1.0, tk.END)
        response_box.insert(tk.END, response)

    send_button = tk.Button(root, text="Send", command=on_send)
    send_button.pack(pady=10)

    root.mainloop()

create_app()