def get_ai_response(title, body):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    
    # This prompt forces the AI to find different case types but keep the format short
    prompt = f"""
    Act as a Senior QA Engineer. Analyze the ticket below and generate test cases.
    
    FOR EACH CASE (Positive, Negative, and Edge Cases), provide ONLY:
    1. Test Case ID (Format: TC-00X - [Short Title])
    2. Test Case Description (A brief summary of the objective)

    STRICT RULES:
    - SKIP Steps, Expected Results, and Preconditions.
    - Group them clearly under headers: ### Positive Cases, ### Negative Cases, and ### Edge Cases.
    - Ensure at least 2 scenarios for each category if the ticket scope allows.

    TICKET TITLE: {title}
    TICKET DESCRIPTION: {body}
    """
    
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2
    }
    
    response = requests.post(url, json=data, headers=headers)
    return response.json()['choices'][0]['message']['content']
