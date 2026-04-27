def get_ai_response(title, body):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    
    # This prompt is strictly designed for high-level scenarios only
    prompt = f"""
    Act as a Senior QA Engineer. Read the GitHub ticket below and provide ONLY a high-level list of Test Scenarios.

    STRICT RULES:
    1. DO NOT include Test Case IDs (like TC-LGN-001).
    2. DO NOT include Steps, Expected Results, or Preconditions.
    3. DO NOT include Environment, Objectives, or Conclusions.
    4. Provide ONLY the scenario titles in a simple bulleted list.
    5. Group them briefly by Positive, Negative, and Edge Cases.

    TICKET TITLE: {title}
    TICKET DESCRIPTION: {body}
    """
    
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2  # Very low temperature makes the AI follow instructions strictly
    }
    
    response = requests.post(url, json=data, headers=headers)
    return response.json()['choices'][0]['message']['content']
