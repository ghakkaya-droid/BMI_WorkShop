import tkinter

window=tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=30, pady=30)

def calculate_BMI():
    height = height_input.get()
    weight = weight_input.get()

    if weight == "" or height == "":
        result_label.config(text="Please enter both height and weight !")

    else:
        try:
            bmi = float(weight) / ((float(height)/100) ** 2)
            result_string = write_result(bmi)
            print(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid Number both height and weight !")


#ui (User interface)
weight_input_label = tkinter.Label(text="Enter your weight (kg)", font=("Arial", 9))
weight_input_label.pack()

weight_input = tkinter.Entry(width=10)
weight_input.pack()

height_input_label = tkinter.Label(text="Enter your height (cm)", font=("Arial", 9))
height_input_label.pack()

height_input = tkinter.Entry(width=10)
height_input.pack()

calculate_button = tkinter.Button(text="Calculate",command=calculate_BMI)
calculate_button.pack()

result_label = tkinter.Label()
result_label.pack()

def write_result (BMI):
    result_string = f"Your BMI is: {round(BMI,2)}. You are "
    if BMI <= 16:
        result_string += "severyly thin"
    elif 16< BMI <= 17:
        result_string += "moderately thin "
    elif 17< BMI <= 18.5:
        result_string += "mid thin "
    elif 18.5< BMI <= 25:
        result_string += "normal"
    elif 25< BMI <= 30:
        result_string += "overweight"
    elif 30< BMI <= 35:
        result_string += "obese class-I"
    elif 35< BMI <= 40:
        result_string += "obese class-II"
    else:
        result_string += "obese class-III"
    return result_string





window.mainloop()