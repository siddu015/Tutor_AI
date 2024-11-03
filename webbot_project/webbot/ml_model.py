# webbot/ml_model.py

import wolframalpha
import wikipedia
from transformers import pipeline

# Initialize models and clients
wolfram_client = wolframalpha.Client("972AR5-4P7L97GLGJ")
qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2")
nlp_generator = pipeline("text-generation", model="gpt2")


def predict(query):

    """Generates an answer for a given query using WolframAlpha, Wikipedia, or NLP models."""

    # First, try WolframAlpha for structured queries (math, science, factual data).
    try:
        res = wolfram_client.query(query)
        ans = next(res.results).text
        return ans
    except Exception as e:
        print(f"WolframAlpha error: {e}")

    # If WolframAlpha fails, try Wikipedia for general knowledge and factual queries.
    try:
        ans = wikipedia.summary(query, sentences=3)
        return ans
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Wikipedia disambiguation error: {e}")
        options = e.options[:5]
        return f"Wikipedia may refer to: {', '.join(options)}"
    except wikipedia.exceptions.PageError as e:
        print(f"Wikipedia page error: {e}")
        return "No information found in Wikipedia."
    except Exception as e:
        print(f"Other Wikipedia error: {e}")

    # If Wikipedia fails, use an open-source NLP QA model (e.g., RoBERTa on SQuAD dataset).
    try:
        qa_result = qa_model(question=query, context="Context could be educational material, textbooks, etc.")
        if qa_result["score"] > 0.5:
            return qa_result["answer"]
    except Exception as e:
        print(f"QA model error: {e}")

    # If all else fails, fall back to a general text generation model (GPT-2) for a best guess.
    try:
        gen_result = nlp_generator(query, max_length=50, num_return_sequences=1)
        return gen_result[0]["generated_text"]
    except Exception as e:
        print(f"Text generation model error: {e}")

    # If none of the sources work, return a default response.
    return "I'm sorry, but I couldn't find an answer to your question."
