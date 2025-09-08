import requests
print('hello jobbot')
# slcak webhook
webhook_url = "https://hooks.slack.com/services/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"

def post_job(title, company, link):
    message = {
        "text": f"*New Job Posting!*\n*{title}* at {company}\n<{link}|Apply Here>"
    }
    requests.post(webhook_url, json=message)

# Example usage
post_job("meow testestest Intern", "TechCorp", "https://jobs.example.com/123")
