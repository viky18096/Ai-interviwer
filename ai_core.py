import openai

openai.api_key = "your-openai-key"  # Or use Streamlit secrets

def generate_question_response(question, response):
    prompt = f"""You are an intelligent political interviewer.
Q: {question}
A: {response}
Give a follow-up or probing question."""
    
    completion = openai.ChatCompletion.create(
        model="gpt-4",  # Replace with "phi-4-multimodal-instruct" if available via API
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message["content"]

def extract_claims(text):
    prompt = f"""Extract bullet-point factual claims from the following:
{text}"""
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message["content"]
