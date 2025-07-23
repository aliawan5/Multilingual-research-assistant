# from tools.translation import MultilingualTranslator
# from tools.google_search import GoogleSearchTool


# translator = MultilingualTranslator()
# search_tool = GoogleSearchTool()

# text_en, lang = translator.process_input("¿Qué es inteligencia artificial?")
# result = search_tool.run(text_en)
# output = translator.process_output(result, lang)
# print(output)
# print(lang)

from tools.translation import MultilingualTranslator
from tools.google_search import GoogleSearchTool
from tools.youtube_tool import YouTubeTranscriptTool


def main():
    translator = MultilingualTranslator()
    search_tool = GoogleSearchTool()
    yt_tool = YouTubeTranscriptTool()

    user_input = input("Ask me anything (you can paste a YouTube link too):\n> ")

    if "youtube.com" in user_input or "youtu.be" in user_input:
        print("Detected YouTube link")
        transcript = yt_tool.extract_transcript(user_input)

        if transcript.startswith("[Error]"):
            print(transcript)
            return

        summary = f"[AI Summary of Video]:\n{transcript[:500]}..."
        print(summary)

    else:
        text_en, lang = translator.process_input(user_input)

        print(f"Detected Language: {lang}")
        print(f"Translated to English: {text_en}")

        google_results = search_tool.run(text_en)
        print(f"Google Results:\n{google_results}")

        youtube_links = yt_tool.search_youtube_links(text_en)
        if youtube_links and not youtube_links[0].startswith("[Error"):
            print(f"Top YouTube Video: {youtube_links[0]}")
            transcript = yt_tool.extract_transcript(youtube_links[0])
            summary = f"[AI Summary of YouTube Video]:\n{transcript[:500]}..."  
        else:
            summary = "No relevant YouTube video found or failed to fetch transcript."


        combined_output = f"{google_results}\n\n{summary}"
        final_output = translator.process_output(combined_output, lang)

        print(f"Final Response (in {lang}):\n{final_output}")


if __name__ == "__main__":
    main()
