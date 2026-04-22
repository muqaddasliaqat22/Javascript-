def get_ai_response(title, body):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    
    # NEW SHORT PROMPT
    prompt = f"""
    Act as a Senior QA Engineer. Based on the ticket below, provide ONLY a bulleted list of 
    Test Scenarios. 
    - Do NOT include 'Steps to Reproduce'.
    - Do NOT include 'Expected Results' or 'Preconditions'.
    - Just list the high-level scenario titles (Positive, Negative, and Edge cases).

    TICKET TITLE: {title}
    TICKET DESCRIPTION: {body}
    """
    
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5 # Lower temperature makes the AI more focused
    }
    
    response = requests.post(url, json=data, headers=headers)
    return response.json()['choices'][0]['message']['content']
