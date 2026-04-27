def get_ai_response(title, body):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    
    # This prompt forces the AI to stop after the first 3 lines
    prompt = f"""
    Act as a Senior QA Engineer. Based on the ticket below, generate ONLY the following three fields and NOTHING ELSE:
    1. Test Case ID (Format: TC-[KEYWORD]-[NUMBER])
    2. Component (The main part of the app mentioned)
    3. Description (A one-sentence summary of the test objective)

    STRICT RULES:
    - DO NOT include Preconditions.
    - DO NOT include Steps.
    - DO NOT include Expected Results.
    - DO NOT include any other text or summary.

    TICKET TITLE: {title}
    TICKET DESCRIPTION: {body}
    """
    
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1  # Set very low for maximum strictness
    }
    
    response = requests.post(url, json=data, headers=headers)
    return response.json()['choices'][0]['message']['content']
