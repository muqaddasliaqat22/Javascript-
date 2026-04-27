def get_ai_response(title, body):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    
    # The prompt is now strictly limited to ID and Description only
    prompt = f"""
    Act as a Senior QA Engineer. Based on the ticket below, write ONLY the Test Case ID and the Description.
    
    STRICT RULES:
    1. Output ONLY 'Test Case ID' and 'Test Case Description'.
    2. SKIP all other info: No Preconditions, No Steps, No Expected Results, No Environment, No Conclusions.
    3. Do NOT use bullet points or bold text for the ID and Description if you want it to look exactly like your example.
    4. Provide the result for each relevant test case identified in the ticket scope.

    TICKET TITLE: {title}
    TICKET DESCRIPTION: {body}
    """
    
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1
    }
    
    response = requests.post(url, json=data, headers=headers)
    return response.json()['choices'][0]['message']['content']
