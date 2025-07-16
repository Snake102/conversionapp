# import required libraries
import tkinter

# create the window
window = tkinter.Tk() # instance
window.title("MilesMeter: Mile(s) to Km Converter") # application title
window.config(background="white",padx=10,pady=10) # background color, padding
window.minsize(300,100) # height

# create a miles label
miles_label = tkinter.Label()
miles_label["text"] = "Miles"
miles_label.config(bg='white', fg='black',font = ("Courier New", 15))
miles_label.grid(row=1,column=3)

# create a text entry box to collect miles
miles_input = tkinter.Entry()
miles_input.grid(row=1,column=2)
miles_input.config(bg='white', fg='black',font = ("Courier New", 15),width=5)

# is equal to label
equal_to_label = tkinter.Label()
equal_to_label["text"] = "is equal to"
equal_to_label.config(bg='white', fg='black',font = ("Courier New", 15))
equal_to_label.grid(row=3,column=0)

# result label
result_label = tkinter.Label()
result_label["text"] = "0"
result_label.config(bg='white', fg='black',font = ("Courier New", 15))
result_label.grid(row=3,column=2)

# result label
km_label = tkinter.Label()
km_label["text"] = "Km(s)"
km_label.config(bg='white', fg='black',font = ("Courier New", 15))
km_label.grid(row=3,column=3)


# submit button event handler
def submit_button_event_handler():

    miles = 0
    km = 0
    CONVERTER = 1.609344

    if miles_input.get() == "": # if user entered an empty string then handle by setting it to default 0
        result_label["text"] = 0
        pass
    else:
        miles = int(miles_input.get()) # convert to int
        km = int(round(miles * CONVERTER,0)) # convert to km and then convert to int to lose the decimals
        result_label['text'] = km # set the result value to the conversion


# submit button - create
submit_button = tkinter.Button()
submit_button.config(text="Calculate", height= 2,bd =0,highlightbackground="white", command=submit_button_event_handler)
submit_button.grid(row=4,column=2)

# run a constant while loop to keep the window listening
window.mainloop()