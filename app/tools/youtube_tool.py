import os
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv

load_dotenv()

class YouTubeTranscriptTool:
    def __init__(self):
        self.serper_api = os.getenv("SERPER_API_KEY")
        self.serper_url = "https://google.serper.dev/search"
        self.headers = {
            "X-API-KEY": self.serper_api,
            "Content-Type": "application/json"
        }


    def search_youtube_links(self, topic: str, lang: str = "en") -> list[str]:
        query = f"{topic} site:youtube.com"
        try:
            response = requests.post(self.serper_url, headers=self.headers, json={"q": query})
            results = response.json().get("organic", [])
            youtube_links = [
                res["link"]
                for res in results
                if "youtube.com" in res.get("link", "") or "youtu.be" in res.get("link", "")
            ]
            return youtube_links[:2] if youtube_links else []
        except Exception as e:
            return [f"[Error fetching YouTube links: {e}]"]



    def extract_transcript(self, video_url: str) -> str:
        try:
            video_id = self._extract_video_id(video_url)
            for lang in ['en', 'es', 'hi', 'ur', 'auto']:
                try:
                    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
                    return " ".join([entry["text"] for entry in transcript])
                except:
                    continue
            return "[Error] Transcript not available in supported languages."
        except Exception as e:
            return f"[Error] Could not fetch transcript: {str(e)}"



    def _extract_video_id(self, url: str) -> str:
        if "v=" in url:
            return url.split("v=")[-1].split("&")[0]
        elif "youtu.be/" in url:
            return url.split("youtu.be/")[-1].split("?")[0]
        else:
            raise ValueError("Invalid YouTube URL format.")
