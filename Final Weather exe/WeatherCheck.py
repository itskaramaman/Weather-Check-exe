from tkinter import *
from datetime import datetime
from tkinter import messagebox


def tell_weather():

    import requests
    api_key = "c33a5e6e30c9964f16a161750e1ff69d"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = cnentry.get()
    if city_name != "":
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        json_data = requests.get(complete_url).json()
        try:
            temp = json_data["main"]["temp"] - 273.15
            tempC = round(temp, 2)

            tempF = (tempC * 1.8) + 32
            tempF = round(tempF, 2)

            global anst_label

            try:
                if anst_label.winfo_ismapped():
                    anst_label.pack_forget()
            except:
                pass

            temp_text = "Right now temperature is " + str(tempC) + " degrees Celcius or " + str(tempF) + " Fahrenheit"
            anst_label = Label(temp_frame, text=temp_text)
            anst_label.pack(side=LEFT, padx=50, pady=10)

            global ansd_label

            try:
                if ansd_label.winfo_ismapped():
                    ansd_label.pack_forget()
            except:
                pass

            desc_text = "Weather is " + str(json_data['weather'][0]['description'])
            ansd_label = Label(desc_frame, text=desc_text)
            ansd_label.pack(side=LEFT, padx=52, pady=10)

            global ansh_label

            try:
                if ansh_label.winfo_ismapped():
                    ansh_label.pack_forget()
            except:
                pass

            hum_text = "Today humidity is " + str(json_data['main']['humidity']) + " g/m3"
            ansh_label = Label(hum_frame, text=hum_text)
            ansh_label.pack(side=LEFT, padx=52, pady=10)

        except:
            messagebox.showerror("Error", "City not Found \n" + "Please enter a valid City name")
            cnentry.delete(0, END)

    else:
        messagebox.showinfo("Info", "Please enter the city name first")
        cnentry.focus_set()


def clear():
    cnentry.delete(0, END)
    cnentry.focus_set()
    try:
        ansh_label.pack_forget()
        ansd_label.pack_forget()
        anst_label.pack_forget()
    except:
        pass


root = Tk()
root.geometry("575x300")
root.configure(background="orange")
root.title("Weather Check")

# toolbar
toolbar = Frame(root, bg='orange')
toolbar.pack(side=TOP, fill=X)
clearButton = Button(toolbar, text="Clear", command=clear)
clearButton.pack(side=LEFT, padx=10, pady=5)

# first part
main = Frame(root)
main.pack(side=TOP)
cnlabel = Label(main, text="City name", bg='green', fg='white')
cnlabel.grid(padx=30, pady=10, row=5, column=2)
cnentry = Entry(main)
cnentry.grid(padx=5, row=5, column=4)


# temperature
temp_frame = Frame(root, bg="orange")
temp_frame.pack(side=TOP, fill=X)

temp_label = Label(temp_frame, text="Temperature")
temp_label.pack(side=LEFT, padx=5, pady=15)


# description
desc_frame = Frame(root, bg='orange')
desc_frame.pack(side=TOP, fill=X)

description_label = Label(desc_frame, text="Description")
description_label.pack(side=LEFT, padx=5, pady=15, ipadx=3)


# humidity
hum_frame = Frame(root, bg="orange")
hum_frame.pack(side=TOP, fill=X)

humidity_label = Label(hum_frame, text="Humidity")
humidity_label.pack(side=LEFT, padx=5, pady=15, ipadx=8)


# status bar
status_bar_frame = Frame(root)
status_bar_frame.pack(side=BOTTOM, fill=X)
status_bar_label = Label(status_bar_frame, text="Karamjeet Singh Production", bd=1, anchor=W)
status_bar_label.pack(side=LEFT)
x = datetime.date(datetime.now())
date = Label(status_bar_frame, text=x)
date.pack(side=RIGHT)

ckbutton = Button(main, text='Check..', command=tell_weather)
ckbutton.grid(padx=10, row=5, column=6)


root.mainloop()
