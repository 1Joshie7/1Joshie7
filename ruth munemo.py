import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime
import json
import os

# Sample user data (username: password)
users = {
    "ruth": "munemo",
    "rachie": "munemo",
    "ano": "munemo",
}

# File to store subjects
DATA_FILE = "subjects.json"

# Main application class
class LessonSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lesson Scheduler")
        self.root.geometry("500x500")  # Set the window size
        self.teacher_subjects = {}
        self.current_teacher = None
        
        # Load existing subjects
        self.load_subjects()
        
        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        self.login_frame = tk.Frame(self.root, padx=10, pady=10)
        self.login_frame.pack(pady=20)

        tk.Label(self.login_frame, text="Username:", font=("Arial", 12)).grid(row=0, column=0, sticky="e")
        self.username_entry = tk.Entry(self.login_frame, font=("Arial", 12))
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.login_frame, text="Password:", font=("Arial", 12)).grid(row=1, column=0, sticky="e")
        self.password_entry = tk.Entry(self.login_frame, show='*', font=("Arial", 12))
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.authenticate_user, font=("Arial", 12))
        self.login_button.grid(row=2, columnspan=2, pady=10)

        self.action_frame = tk.Frame(self.root)

    def authenticate_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in users and users[username] == password:
            self.current_teacher = username
            messagebox.showinfo("Login", "Login successful!")
            self.login_frame.pack_forget()
            self.show_action_buttons()
        else:
            messagebox.showerror("Login", "Invalid username or password. Please try again.")

    def show_action_buttons(self):
        self.action_frame.pack(pady=20)

        self.add_button = tk.Button(self.action_frame, text="Add Subject", command=self.get_subject_details, font=("Arial", 12))
        self.add_button.pack(pady=10)

        self.view_button = tk.Button(self.action_frame, text="View Subjects", command=self.display_subject_details, font=("Arial", 12))
        self.view_button.pack(pady=10)

        self.search_button = tk.Button(self.action_frame, text="Search Subject", command=self.search_subject, font=("Arial", 12))
        self.search_button.pack(pady=10)

        self.logout_button = tk.Button(self.action_frame, text="Logout", command=self.logout, font=("Arial", 12))
        self.logout_button.pack(pady=10)

    def load_subjects(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                self.teacher_subjects = json.load(f)

    def save_subjects(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self.teacher_subjects, f)

    def get_subject_details(self):
        subject_name = simpledialog.askstring("Input", "Enter the subject name:", parent=self.root)
        subject_time = simpledialog.askstring("Input", "Enter the subject time (HH:MM):", parent=self.root)
        subject_date = simpledialog.askstring("Input", "Enter the subject date (YYYY-MM-DD):", parent=self.root)
        lesson_objectives = simpledialog.askstring("Input", "Enter the lesson objectives:", parent=self.root)
        teacher_name = simpledialog.askstring("Input", "Enter the teacher's name:", parent=self.root)
        class_name = simpledialog.askstring("Input", "Enter the class for the subject:", parent=self.root)

        # Validate and convert date and time
        try:
            subject_time = datetime.datetime.strptime(subject_time, "%H:%M").time()
            subject_date = datetime.datetime.strptime(subject_date, "%Y-%m-%d").date()
            subject_details = {
                "subject_name": subject_name,
                "subject_time": subject_time.isoformat(),
                "subject_date": subject_date.isoformat(),
                "lesson_objectives": lesson_objectives,
                "teacher_name": teacher_name,
                "class_name": class_name
            }

            if self.current_teacher not in self.teacher_subjects:
                self.teacher_subjects[self.current_teacher] = []
            self.teacher_subjects[self.current_teacher].append(subject_details)
            self.save_subjects()
            messagebox.showinfo("Success", "Subject added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid date or time format. Please try again.")

    def display_subject_details(self):
        if self.current_teacher in self.teacher_subjects:
            subjects = self.teacher_subjects[self.current_teacher]
            subject_list = "\n".join([
                f"Subject Name: {sub['subject_name']}\n"
                f"Subject Time: {sub['subject_time']}\n"
                f"Subject Date: {sub['subject_date']}\n"
                f"Lesson Objectives: {sub['lesson_objectives']}\n"
                f"Teacher Name: {sub['teacher_name']}\n"
                f"Class: {sub['class_name']}\n"
                for sub in subjects
            ])
            messagebox.showinfo("Subjects", subject_list)
        else:
            messagebox.showinfo("Subjects", "No subjects found for this teacher.")

    def search_subject(self):
        subject_name = simpledialog.askstring("Search", "Enter the subject name to search:", parent=self.root)
        if self.current_teacher in self.teacher_subjects:
            subjects = self.teacher_subjects[self.current_teacher]
            found_subjects = [sub for sub in subjects if sub['subject_name'].lower() == subject_name.lower()]
            if found_subjects:
                subject_list = "\n".join([
                    f"Subject Name: {sub['subject_name']}\n"
                    f"Subject Time: {sub['subject_time']}\n"
                    f"Subject Date: {sub['subject_date']}\n"
                    f"Lesson Objectives: {sub['lesson_objectives']}\n"
                    f"Teacher Name: {sub['teacher_name']}\n"
                    f"Class: {sub['class_name']}\n"
                    for sub in found_subjects
                ])
                messagebox.showinfo("Search Results", subject_list)
            else:
                messagebox.showinfo("Search Results", "No subjects found with that name.")
        else:
            messagebox.showinfo("Search Results", "No subjects found for this teacher.")

    def logout(self):
        self.current_teacher = None
        self.action_frame.pack_forget()
        self.login_frame.pack(pady=20)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

# Main function to run the application
def main():
    root = tk.Tk()
    app = LessonSchedulerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()