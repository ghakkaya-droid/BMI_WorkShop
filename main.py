from tkinter import *

#Variables

window = Tk()
Label_info = Label(text="Vücut Kitle İndeksi Hesaplama",font="normal")
Label_Text_Weight = Label(text="Ağırlığınızı kg olarak giriniz:")
Label_Text_Height = Label(text="Boyunuzu 'cm' olarak giriniz:")
Entry_weight = Entry()
Entry_height = Entry()
RESULT =0
Label_Result = Label(text=RESULT)

#Ana Ekran Ayarları ve Görünüm

window.title("BMI")
window.minsize(400, 300)

Label_info.config(font=("Arial", 12,"underline"))
Label_info.pack()
Label_info.place(x=10, y=10)
Label_info.update()
Xcor=Label_info.winfo_width()
Ycor=Label_info.winfo_height()
Label_info.place(x=400/2-Xcor/2, y=10)

Label_Text_Weight.place(x=1000,y=1000)
Label_Text_Weight.update()
Xcor=Label_Text_Weight.winfo_width()
Label_Text_Weight.place(x=30, y=50)

Entry_weight.config(font=("Arial", 12))
Entry_weight.config(width=10)
Entry_weight.place(x=50+Xcor+10,y=50)

Label_Text_Height.place(x=30, y=100)

Entry_height.config(font=("Arial", 12))
Entry_height.config(width=10)
Entry_height.place(x=50+Xcor+10,y=100)



#BMI hesaplama
def BMI_Calculate():
    global RESULT
    global Label_Result
    Label_Result.config(text="",bg="SystemButtonFace")
    if Entry_weight.get().strip() == "" or Entry_height.get().strip() == "":
        Label_Result.config(text="Lütfen Sayı giriniz !!!", fg="red")
        Label_Result.place(x=200, y=200)
        return
    if not Entry_weight.get().isdigit() or not Entry_height.get().isdigit():
        Label_Result.config(text="Lütfen Sayı giriniz !!!", fg="red")
        Label_Result.place(x=200, y=200)
        return

    W = float(Entry_weight.get())
    H = float(Entry_height.get())
    H=H/100
    RESULT = W/(H*H)
    print(RESULT)
    Calculate_Button.config(text=f"BMI = {RESULT:.2f}")
    if RESULT <=18.5 :
        Label_Result.config(text="Düşük Kilolu", fg="red",bg="light grey")
        Label_Result.place(x=200, y=200)
        Label_Result.place(x=200, y=200)
        Label_Result.place(x=200, y=200)
    elif 18.5 < RESULT <= 24.9 :
        Label_Result.config(text="Normal Kilolu", fg="Green",bg="light grey")
        Label_Result.place(x=200, y=200)
    elif 24.9 < RESULT <= 29.9:
        Label_Result.config(text="Fazla Kilolu", fg="yellow",bg="dark grey")
        Label_Result.place(x=200, y=200)
    elif 24.9 < RESULT <= 40:
        Label_Result.config(text="OBEZ !", fg="Red",bg="SystemButtonFace")
        Label_Result.place(x=200, y=200)
    elif RESULT > 40:
        Label_Result.config(text="AŞIRI OBEZ !!!", fg="Red",bg="SystemButtonFace")
        Label_Result.place(x=200, y=200)


Calculate_Button = Button(text="Hesapla",command=BMI_Calculate,width=15)
Calculate_Button.place(x=1000, y=1000)
Xcor=Calculate_Button.winfo_width()
Calculate_Button.place(x=400/2-Xcor/2, y=150)
print(window["bg"])









window.mainloop()