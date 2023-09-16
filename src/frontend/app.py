# Import required Libraries
import customtkinter as ctk
from PIL import Image
import cv2

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")


class App(ctk.CTk):
    # Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Sets the title of our window to "PostSURE"
        self.title("PostSURE")
        # Dimensions of the window will be 1280x600
        self.geometry("1280x600")
        self.resizable(False, False)


class StarterFrame(ctk.CTkFrame):
    def __init__(self, container):
        super().__init__(container)
        self.grid(row=0, column=0)
        video_frame = ctk.CTkFrame(master=self, width=680, height=520)
        video_frame.propagate(False)
        video_frame.grid(row=0, column=0, padx=(60, 30), pady=60)

        video = ctk.CTkLabel(master=video_frame, text="")
        video.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        gui_frame = ctk.CTkFrame(master=self, width=420, height=520)
        gui_frame.grid(row=0, column=1, padx=(30, 60), pady=20)

        header = ctk.CTkLabel(master=gui_frame, text="Welcome to PostSURE!",
                              font=('Tw Cen MT Condensed Extra Bold', 60), wraplength=400)
        header.place(relx=0.5, rely=0.17, anchor=ctk.CENTER)

        dialogue_frame = ctk.CTkFrame(master=gui_frame, width=380, height=320)
        dialogue_frame.place(relx=0.5, rely=0.96, anchor=ctk.S)

        cap = cv2.VideoCapture(0)

        def show_frames():
            # Get the latest frame and convert into Image
            cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            # Convert image to PhotoImage
            imgtk = ctk.CTkImage(img, size=(640, 480))
            video.imgtk = imgtk
            video.configure(image=imgtk)
            # Repeat after an interval to capture continuously
            video.after(20, show_frames)

        show_frames()


if __name__ == "__main__":
    app = App()
    StarterFrame(app)
    app.mainloop()