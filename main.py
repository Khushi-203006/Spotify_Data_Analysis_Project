#import the json library
#used to read data stored in JSON format
import json

#Import pandas library 
#Pandas helps us work with tables
import pandas as pd

#Import tkinter gui components
#Tk - creates window
#filedialog - opens file picker
#messagebox = shows popup messages

from tkinter import Tk , filedialog , messagebox

#Import os module
#used for file and folder operations
import os


#create a tkinter window object
root = Tk()

#hide the empty tkinter window
#we only want the file picker , not a blank window
#root.withdraw() - hides the main window of the tkinter app
root.withdraw()

#open a file selection dialog 
json_file = filedialog.askopenfilename(

    #title displayed on top of file picker
    title = "Select json file",

    #only show .json files
    #filetypes formate = (display name, file extension)
    filetypes = [("Json files", "*.json")]
)

#check if user clicked cancel
if not json_file:

    #Print message in terminal
    print("No file selected.")

    #stop the program
    exit()

#try block - if error occurs, execution jumps to except block
try:

    #open selected json file
    #json_file = path selected by user
    #r - read mode
    #utf-8 handles special characters safely
    with open(json_file , "r" , encoding = "utf-8") as f:

        #read json data and store in variable
        data = json.load(f)

    #convert JSON data into a pandas dataframe
    #dataframe = spreadsheet - like table

    df = pd.DataFrame(data)

    # create output csv filename

    #example
    #input = xyz.JSON 

    #output = zyx.csv

    csv_file = os.path.splitext(json_file)[0] + ".csv"

    #save dataframe as CSV
    df.to_csv(csv_file, index=False) 

    #show success popup
    messagebox.showinfo(

        #popup title
        "Success",

        #popup message
        f" Your CSV file is ready!\n Kindly check \n{csv_file}"
    )

#if any error occurs
except Exception as e:

    #show error popup
    messagebox.showerror(

        #popup title
        "Error",

        #display actual error message
        str(e)
    )
    


