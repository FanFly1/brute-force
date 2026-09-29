import random
import string
import tkinter as tk
import time

all_symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits

root = tk.Tk()
root.title("BruteForce")
root.geometry("400x400")

attempt = 0
def startBruteForce():
    word = entrylbl2.get()
    lenofword = len(word)
    attempt = 0
    start_time = time.time()
    

    while True:
        guess = ""
        attempt = attempt + 1
        for i in range(lenofword):
            guess = guess + random.choice(all_symbols)
            
        if guess == word:
            end_time = time.time()
            real_time = end_time - start_time
            lblresult.config(text=f"Угадано, отгадали: {guess}, а ваше слово {word}, угадали за {real_time:.2f}")
            break
        else:
            if attempt % 100000 == 0:
                current_time = time.time() - start_time
                lblresult.config(text=f"Попытка номер {attempt}, время: {current_time:.2f}, вариант: {guess}")
                root.update()

lbl1 = tk.Label(root, text="Введите слово для взлома", font=("Arial", 18), fg="black")
lbl1.pack(pady=10)

entrylbl2 = tk.Entry(root, font=("Arial", 16))
entrylbl2.insert(0,"car")
entrylbl2.pack(pady=14)

button = tk.Button(root, text="Нажмите для начала брутфорса", font=("Arial", 15), bg="green", fg="white", command=startBruteForce)
button.pack(pady=15)

lblresult = tk.Label(root, text="", font=("Arial", 18), fg="black")
lblresult.pack(pady=15)

root.mainloop()