def get_ai_response(title, body):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    
    # This prompt tells the AI to provide ONLY the list of check-style scenarios
    prompt = f"""
    Act as a Senior QA Engineer. Based on the ticket below, write a simple list of test scenarios.
    
    STRICT RULES:
    1. Start every line with "Check " followed by the scenario.
    2. Provide ONLY the list of scenarios. 
    3. DO NOT include "Test Case ID", "Component", "Steps", or "Expected Results".
    4. DO NOT include any introductory or concluding text.
    5. Include scenarios for responsiveness and cross-browser testing at the end.

    TICKET TITLE: {title}
    TICKET DESCRIPTION: {body}
    """
    
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1  # Low temperature ensures it sticks to the format
    }
    
    response = requests.post(url, json=data, headers=headers)
    return response.json()['choices'][0]['message']['content']
