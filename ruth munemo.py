import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime

# Sample user data (username: password)
users = {
    "ruth": "munemo",
    "rachie": "munemo",
    "ano": "munemo",
}

# Main application class
class LessonSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lesson Scheduler")
        self.teacher_subjects = {}
        self.current_teacher = None
        
        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(pady=10)

        tk.Label(self.login_frame, text="Username:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.login_frame, text="Password:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show='*')
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.authenticate_user)
        self.login_button.grid(row=2, columnspan=2, pady=5)

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
        self.action_frame.pack(pady=10)

        self.add_button = tk.Button(self.action_frame, text="Add Subject", command=self.get_subject_details)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(self.action_frame, text="View Subjects", command=self.display_subject_details)
        self.view_button.pack(pady=5)

        self.logout_button = tk.Button(self.action_frame, text="Logout", command=self.logout)
        self.logout_button.pack(pady=5)

    def get_subject_details(self):
        subject_name = simpledialog.askstring("Input", "Enter the subject name:")
        subject_time = simpledialog.askstring("Input", "Enter the subject time (HH:MM):")
        subject_date = simpledialog.askstring("Input", "Enter the subject date (YYYY-MM-DD):")
        lesson_objectives = simpledialog.askstring("Input", "Enter the lesson objectives:")
        teacher_name = simpledialog.askstring("Input", "Enter the teacher's name:")

        # Validate and convert date and time
        try:
            subject_time = datetime.datetime.strptime(subject_time, "%H:%M").time()
            subject_date = datetime.datetime.strptime(subject_date, "%Y-%m-%d").date()
            subject_details = {
                "subject_name": subject_name,
                "subject_time": subject_time,
                "subject_date": subject_date,
                "lesson_objectives": lesson_objectives,
                "teacher_name": teacher_name  # Store the teacher's name
            }

            if self.current_teacher not in self.teacher_subjects:
                self.teacher_subjects[self.current_teacher] = []
            self.teacher_subjects[self.current_teacher].append(subject_details)
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
                f"Teacher Name: {sub['teacher_name']}\n"  # Display the teacher's name
                for sub in subjects
            ])
            messagebox.showinfo("Subjects", subject_list)
        else:
            messagebox.showinfo("Subjects", "No subjects found for this teacher.")

    def logout(self):
        self.current_teacher = None
        self.action_frame.pack_forget()
        self.login_frame.pack(pady=10)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

# Main function to run the application
def main():
    root = tk.Tk()
    app = LessonSchedulerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()