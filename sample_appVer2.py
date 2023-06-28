from PyDictionary import PyDictionary
from gtts import gTTS
import tkinter as tk
import os

# PyDictionaryの初期化
dictionary = PyDictionary()

# 発音を再生する関数
def play_pronunciation(word):
    pronunciation = dictionary.meaning(word)
    if pronunciation:
        pronunciation_text = pronunciation[list(pronunciation.keys())[0]][0]
        tts = gTTS(pronunciation_text)
        pronunciation_filepath = "pronunciation.mp3"
        tts.save(pronunciation_filepath)
        os.system(f"afplay {pronunciation_filepath}")  # macOSの場合の再生コマンド
        os.remove(pronunciation_filepath)  # ファイルを削除
    else:
        print("発音が見つかりませんでした。")

# 単語の意味を取得して表示する関数
def get_meaning(word):
    meanings = dictionary.meaning(word)
    if meanings:
        meaning_text = ""
        for part_of_speech, meaning_list in meanings.items():
            meaning_text += f"{part_of_speech}:\n"
            for meaning in meaning_list:
                meaning_text += f"- {meaning}\n"
        meaning_label.config(text=meaning_text)
    else:
        meaning_label.config(text="意味が見つかりませんでした。")

# ボタンクリック時の処理
def button_click():
    user_input = entry.get()
    play_pronunciation(user_input)
    get_meaning(user_input)

# ウィンドウの作成
window = tk.Tk()
window.title("英語学習アプリ")

# 入力エリア
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

# ボタン
button = tk.Button(window, text="検索", command=button_click)
button.pack(pady=10)

# 意味表示ラベル
meaning_label = tk.Label(window, wraplength=400)
meaning_label.pack(pady=10)

# ウィンドウの表示
window.mainloop()

