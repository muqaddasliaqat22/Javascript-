import os
import requests
from github import Github

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
TICKET_ID = os.getenv('TICKET_ID')
REPO_NAME = os.getenv('GITHUB_REPOSITORY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

def get_ai_response(title, body):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    
    prompt = f"""
    Act as a Senior QA Engineer. Based on the ticket below, write ONLY the Test Case ID and Description.
    
    STRICT RULES:
    1. Output ONLY 'Test Case ID' and 'Test Case Description'.
    2. SKIP Steps, Expected Results, Preconditions, and all other info.
    3. Format: 
       Test Case ID: TC-00X - [Title]
       Test Case Description: [One sentence description]

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

g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)
issue = repo.get_issue(number=int(TICKET_ID))

test_cases = get_ai_response(issue.title, issue.body)
issue.create_comment(f"### 🤖 Automated Test Cases\n\n{test_cases}")
