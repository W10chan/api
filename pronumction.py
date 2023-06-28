import requests

def get_word_pronunciation(word):
    url = f"https://apifree.forvo.com/key/{YOUR_API_KEY}/format/json/action/word-pronunciations/word/{word}"
    response = requests.get(url)
    data = response.json()
    
    if data["items"]:
        return data["items"][0]["pathmp3"]
    else:
        return None

def play_pronunciation(audio_url):
    # ここでオーディオ再生の実装を行う

word = input("Enter a word: ")
pronunciation_url = get_word_pronunciation(word)

if pronunciation_url:
    play_pronunciation(pronunciation_url)
else:
    print("Pronunciation not available for the word.")