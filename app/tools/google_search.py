import os
import requests
from dotenv import load_dotenv

load_dotenv()


class GoogleSearchTool:
    def __init__(self):
        self.api_key = os.getenv("SERPER_API_KEY")
        self.endpoint = "https://google.serper.dev/search"
        self.headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }

    def run(self, query: str) -> str:
        payload = {"q": query}
        try:
            response = requests.post(self.endpoint, headers=self.headers, json=payload)
            data = response.json()


            if "organic" in data:
                top_results = data["organic"][:3]
                summary = "\n".join([f"- {r['title']}\n  {r['link']}" for r in top_results])
                return summary or "[No useful results]"
            return "[No results found]"
        except Exception as e:
            return f"[Error during web search: {str(e)}]"
