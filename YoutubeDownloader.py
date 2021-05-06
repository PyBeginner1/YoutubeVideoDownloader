from pytube import YouTube
from playsound import playsound
import tkinter as tk

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 200
WINDOW_TITLE = 'Youtube mp3 downloader'
BUTTON_CLICK_SOUND = 'clicks.m4a'


class YoutubeDownload:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.window.title(WINDOW_TITLE)
        self.window.config(bg = "#bacad7")

        #create label
        self.download_label = tk.Label(self.window, text ="Download Link")
        self.download_label.grid(row = 0, column =0, padx =10, pady =5)
        self.download_label.config(bg="#fece9e")
        self.name_label = tk.Label(self.window, text="Save File as ")
        self.name_label.grid(row=1, column=0, pady = 10)
        self.name_label.config(bg="#fece9e")
        self.path_label = tk.Label(self.window, text="Save File Path ")
        self.path_label.grid(row=2, column=0, pady = 10, padx =10)
        self.path_label.config(bg="#fece9e")
        self.ext_label = tk.Label(self.window, text="File Extension ")
        self.ext_label.grid(row=3, column=0, pady = 10, padx =10)
        self.ext_label.config(bg="#fece9e")

        #create entry field
        self.download_entry = tk.Entry(self.window, width =60)
        self.download_entry.grid(row = 0, column = 1, pady = 5)
        self.download_entry.config(bg="#dec4a1")
        self.name_entry = tk.Entry(self.window, width =60)
        self.name_entry.grid(row=1, column=1, pady =10)
        self.name_entry.config(bg="#dec4a1")
        self.path_entry = tk.Entry(self.window, width =60)
        self.path_entry.grid(row=2, column=1)
        self.path_entry.config(bg="#dec4a1")
        self.ext_entry = tk.Entry(self.window, width =60)
        self.ext_entry.grid(row=3, column=1)
        self.ext_entry.config(bg="#dec4a1")

        #create button
        self.download_button = tk.Button(self.window, text = "Download", command = self.get_link)
        self.download_button.grid(row =4, column = 1)
        self.download_button.config(bg = "#d2cbc4")


    def downloader(self, link, save_path="" , save_name="", extension = "mp4"):
        yt = YouTube(link)
        yt_stream = yt.streams.filter(progressive = True, file_extension = extension).order_by('resolution').desc().first()
        yt_stream.download(output_path=save_path, filename=save_name)
        return


    def get_link(self):
        link = self.download_entry.get()
        name = self.name_entry.get()
        path = self.path_entry.get()
        ext = self.ext_entry.get()

        self.downloader(link, path, name, ext)

    def run_app(self):
        self.window.mainloop()
        return



if __name__== "__main__":
    app = YoutubeDownload()
    app.run_app()