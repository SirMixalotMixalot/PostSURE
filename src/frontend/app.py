# Import required Libraries
import customtkinter as ctk
from PIL import Image
import cv2
from pyler import notification 

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")


class App(ctk.CTk):
    # Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Sets the title of our window to "PostSURE"
        self.title("PostSURE")
        self.resizable(False, False)


class StarterFrame(ctk.CTkFrame):
    def __init__(self, container):
        super().__init__(container)
        self.grid(row=0, column=0)
        self.video_frame = ctk.CTkFrame(master=self, width=680, height=520)
        self.video_frame.propagate(False)
        self.video_frame.grid(row=0, column=0, padx=(60, 30), pady=60)

        self.video = ctk.CTkLabel(master=self.video_frame, text="")
        self.video.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        self.gui_frame = ctk.CTkFrame(master=self, width=420, height=520)
        self.gui_frame.grid(row=0, column=1, padx=(30, 60), pady=20)

        self.header = ctk.CTkLabel(master=self.gui_frame, text="Welcome to PostSURE",
                                   font=('Helvetica Bold', 40), wraplength=400)
        self.header.place(relx=0.5, rely=0.17, anchor=ctk.CENTER)

        def change_frame():
            self.intro_frame.place_forget()
            self.outro_frame.tkraise()
            self.outro_frame.place(relx=0.5, rely=0.96, anchor=ctk.S)

        self.intro_frame = ctk.CTkFrame(master=self.gui_frame, width=380, height=320)
        self.intro_frame.place(relx=0.5, rely=0.96, anchor=ctk.S)

        self.intro_prompt = ctk.CTkLabel(master=self.intro_frame, text="Sit up straight!",
                                         font=('Helvetica', 30), wraplength=400)
        self.intro_prompt.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

        self.snapshot = ctk.CTkButton(master=self.intro_frame, width=300, height=150, text="Take snapshot",
                                      font=('Helvetica', 30), command=change_frame)
        self.snapshot.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

        self.outro_frame = ctk.CTkFrame(master=self.gui_frame, width=380, height=320)
        self.outro_frame.place(relx=0.5, rely=0.96, anchor=ctk.S)

        self.outro_prompt = ctk.CTkLabel(master=self.outro_frame, text="Perfect! Press \"Done\" to start working or " +
                                         "\"Retake\" if you're not happy with your snapshot.",
                                         font=('Helvetica', 20), wraplength=400)
        self.outro_prompt.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

        self.retake = ctk.CTkButton(master=self.outro_frame, width=150, height=100, text="Retake",
                                    font=('Helvetica', 30),)
        self.retake.place(relx=0.25, rely=0.6, anchor=ctk.CENTER)
        self.done = ctk.CTkButton(master=self.outro_frame, width=150, height=100, text="Done",
                                  font=('Helvetica', 30),)
        self.done.place(relx=0.75, rely=0.6, anchor=ctk.CENTER)
        self.outro_frame.place_forget()

        cap = cv2.VideoCapture(0)

        def show_frames():
            # Get the latest frame and convert into Image
            cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            # Convert image to PhotoImage
            imgtk = ctk.CTkImage(img, size=(640, 480))
            self.video.imgtk = imgtk
            self.video.configure(image=imgtk)
            # Repeat after an interval to capture continuously
            self.video.after(20, show_frames)

        show_frames()


# class FirstFrame(ctk.CTkFrame):
#     def __init__(self, container):

def notification():
    notification.notify(
    title = 'POSTURE',
    message = 'Your posture is bad',
    app_icon = None,
    timeout = 20,
)


if __name__ == "__main__":
    app = App()
    StarterFrame(app)
    app.mainloop()
