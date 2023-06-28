from PyDictionary import PyDictionary
from gtts import gTTS
from playsound import playsound

# PyDictionaryの初期化
dictionary = PyDictionary()

# 発音を再生する関数
def play_pronunciation(word):
    pronunciation = dictionary.phrase_meaning(word)
    if pronunciation:
        tts = gTTS(pronunciation)
        tts.save("pronunciation.mp3")
        playsound("pronunciation.mp3")
    else:
        print("発音が見つかりませんでした。")

# 単語の意味を取得して表示する関数
def get_meaning(word):
    meanings = dictionary.meaning(word)
    if meanings:
        for part_of_speech, meaning_list in meanings.items():
            print(f"{part_of_speech}:")
            for meaning in meaning_list:
                print("-", meaning)
    else:
        print("意味が見つかりませんでした。")

# メインの処理
while True:
    user_input = input("単語を入力してください（終了するには'q'を入力）: ")
    if user_input.lower() == "q":
        break
    
    play_pronunciation(user_input)
    get_meaning(user_input)
