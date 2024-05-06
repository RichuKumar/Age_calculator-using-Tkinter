
import datetime
import tkinter as tk
import tkinter.messagebox as mbox
from PIL import Image, ImageTk


class AgeCalculator():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Age Calculator')
        self.root.geometry("1199x600+150+100")

        # Add background image
        photo_path = "Pictures/back.png"
        photo_pil = Image.open(photo_path)
        photo_pil_resized = photo_pil.resize((1199, 600))
        self.photo_pil = ImageTk.PhotoImage(photo_pil_resized)
        self.label = tk.Label(self.root, image=self.photo_pil)
        self.label.pack()

        # Add frame
        frame = tk.Frame(self.root, bg="white", bd=5, width=800, height=500, relief="raised")
        frame.place(x=200, y=50)

        # Add input labels and entries for Date of Birth
        tk.Label(frame, text="Date of Birth", font=("Courier New", 15, "bold"), bg="white").place(x=40, y=0)
        self.dob_day_entry = tk.Entry(frame, font=("Times New Roman", 15), bg="white")
        self.dob_day_entry.place(x=70, y=30)
        tk.Label(frame, text="Date:", font=("Times New Roman", 15), bg="white").place(x=0, y=30)

        self.dob_month_entry = tk.Entry(frame, font=("Times New Roman", 15), bg="white")
        self.dob_month_entry.place(x=70, y=70)
        tk.Label(frame, text="Month:", font=("Times New Roman", 15), bg="white").place(x=0, y=70)

        self.dob_year_entry = tk.Entry(frame, font=("Times New Roman", 15), bg="white")
        self.dob_year_entry.place(x=70, y=110)
        tk.Label(frame, text="Year:", font=("Times New Roman", 15), bg="white").place(x=0, y=110)

        # Add input labels and entries for Given Date
        tk.Label(frame, text="Given Date", font=("Courier New", 15, "bold"), bg="white").place(x=530, y=0)
        self.given_day_entry = tk.Entry(frame, font=("Times New Roman", 15), bg="white")
        self.given_day_entry.place(x=510, y=30)
        tk.Label(frame, text="Date:", font=("Times New Roman", 15), bg="white").place(x=440, y=30)

        self.given_month_entry = tk.Entry(frame, font=("Times New Roman", 15), bg="white")
        self.given_month_entry.place(x=510, y=70)
        tk.Label(frame, text="Month:", font=("Times New Roman", 15), bg="white").place(x=440, y=70)

        self.given_year_entry = tk.Entry(frame, font=("Times New Roman", 15), bg="white")
        self.given_year_entry.place(x=510, y=110)
        tk.Label(frame, text="Year:", font=("Times New Roman", 15), bg="white").place(x=440, y=110)

        # Add a button to trigger the age calculation
        button = tk.Button(frame, text="Calculate", relief="raised", bg="red2", bd=2,
                           font=("Comic Sans MS", 15, "bold"), command=self.on_click)
        button.place(x=350, y=200)

        # Add labels and entries for output (final age)
        tk.Label(frame, text="Years:", font=("Times New Roman", 15), bg="white").place(x=250, y=280)
        self.final_years_entry = tk.Entry(frame, font=("Times New Roman", 15), bg="white", bd=2)
        self.final_years_entry.place(x=320, y=280)

        tk.Label(frame, text="Months:", font=("Times New Roman", 15), bg="white").place(x=250, y=320)
        self.final_months_entry = tk.Entry(frame, font=("Times New Roman", 15), bg="white", bd=2)
        self.final_months_entry.place(x=320, y=320)

        tk.Label(frame, text="Days:", font=("Times New Roman", 15), bg="white").place(x=250, y=360)
        self.final_days_entry = tk.Entry(frame, font=("Times New Roman", 15), bg="white", bd=2)
        self.final_days_entry.place(x=320, y=360)

    def on_click(self):
        # Retrieve birth date
        try:
            birth_day = int(self.dob_day_entry.get())
            birth_month = int(self.dob_month_entry.get())
            birth_year = int(self.dob_year_entry.get())
            birthdate = datetime.date(birth_year, birth_month, birth_day)
        except ValueError:
            mbox.showerror("Error", "Invalid birth date. Please enter valid integers.")
            return
        except Exception as e:
            mbox.showerror("Error", f"An error occurred: {str(e)}")
            return

        # Retrieve given date
        try:
            given_day = int(self.given_day_entry.get())
            given_month = int(self.given_month_entry.get())
            given_year = int(self.given_year_entry.get())
            given_date = datetime.date(given_year, given_month, given_day)
        except ValueError:
            mbox.showerror("Error", "Invalid given date. Please enter valid integers.")
            return
        except Exception as e:
            mbox.showerror("Error", f"An error occurred: {str(e)}")
            return

        # Check if given date is earlier than birthdate
        if given_date < birthdate:
            mbox.showerror("Error", "Given date is earlier than birth date.")
            return

    
        age = given_year - birth_year

        # Adjust age if the given birthday has not occured
        if (given_month, given_day) < (birth_month, birth_day):
            age -= 1
        if (given_month, given_day) >= (birth_month, birth_day):
            extra_months = given_month - birth_month
            extra_days = given_day - birth_day
        else:
            if given_month >= birth_month:
                extra_months = given_month - birth_month - 1
            else:
                extra_months = given_month - birth_month + 11

            # Calculate extra days by getting the previous month's days
            previous_month = (given_month - 1) if given_month > 1 else 12
            days_in_previous_month = (datetime.date(given_year, previous_month, 1) - datetime.timedelta(days=1)).day
            extra_days = given_day + (days_in_previous_month - birth_day)

        # Display the calculated age
        self.final_years_entry.delete(0, tk.END)
        self.final_years_entry.insert(0, age)

        self.final_months_entry.delete(0, tk.END)
        self.final_months_entry.insert(0, extra_months)

        self.final_days_entry.delete(0, tk.END)
        self.final_days_entry.insert(0, extra_days)



age_calculator = AgeCalculator()
age_calculator.root.mainloop()

