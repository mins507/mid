# main.py
# 2단계: 메모 입력 및 저장 기능 추가

import tkinter as tk

root = tk.Tk()
root.title("메모장 프로그램")
root.geometry("400x400")

# 텍스트 입력창
text_area = tk.Text(root, wrap='word')
text_area.pack(expand=True, fill='both')

# 저장 함수
def save_memo():
    memo = text_area.get("1.0", tk.END)
    with open("memo.txt", "w", encoding="utf-8") as f:
        f.write(memo)

# 저장 버튼
save_btn = tk.Button(root, text="저장", command=save_memo)
save_btn.pack()

root.mainloop()
