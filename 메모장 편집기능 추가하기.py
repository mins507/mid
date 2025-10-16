# main.py
# 3단계: 파일 열기, 저장 기능 추가 (편집 기능 강화)

import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("메모장 프로그램")
root.geometry("500x500")

# 텍스트 입력창
text_area = tk.Text(root, wrap='word')
text_area.pack(expand=True, fill='both')

# 파일 열기
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, f.read())

# 파일 저장
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text_area.get("1.0", tk.END))
        messagebox.showinfo("저장 완료", "메모가 저장되었습니다!")

# 버튼 영역
frame = tk.Frame(root)
frame.pack(fill='x')

open_btn = tk.Button(frame, text="열기", command=open_file)
open_btn.pack(side='left', padx=5, pady=5)

save_btn = tk.Button(frame, text="저장", command=save_file)
save_btn.pack(side='left', padx=5, pady=5)

root.mainloop()
