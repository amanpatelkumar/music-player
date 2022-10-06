import os
import pickle
import tkinter as tk
from tkinter import HORIZONTAL, filedialog
from typing_extensions import Self
from pygame import mixer

class player(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        mixer.init()

        if os.path.exists('songs.pickle'):
            with open('songs.pickle', 'rb') as f:
                self.playlist = pickle.load(f)
        else:
            self.playlist=[]

         self.current = 0
         self.paused = True
         self.played = False

         self.create_frames()
         self.track_widgets()
         self.control_widgets()
         self.tracklist_widgets()

    def create_frames(self):
        self.track = tk.LabelFrame(self, text="Song TracK", font=("times new roman", 15, "bold"), bg="grey", fg="white", bd=5, relief=tk.GROOVE)

        self.track.config(width=410, height=300)
        self.track.grid(row=0, column=0, padx=10)

        self.tracklist = tk.LabelFrame(self, text=f'Playlist - {str(len(self.playlist))}',font=("times new roman", 15, "bold"), bg= "grey", fg="white", bd= 5, relief=tk.GROOVE)
        self.tracklist.grid(row=0, column=1, rowspan=3, pady=5)

        self.controls = tk.LabelFrame(self, font=("times new roman", 15, "bold"), bg="white", fg="white", bd=2, relief=tk.GROOVE)
        self.controls.config(width=410, height=80)
        self.controls.grid(row=2, column=0, pady=5, padx=10)

    def track_widgets(self):
        self.canvas = tk.Label(self.track, image=img)
        self.canvas.configure(width=400, height=240)
        self.canvas.grid(row=2, column=0)

        self.songtrack = tk.Label(self.track, font=("times new roman",16,"bold"), bg="white",fg="dark blue",)
        self.songtrack['text'] = 'Musicxy MP3 Player'
        self.songtrack.config(width=30, height=1)
        self.songtrack.grid(row=1, column=0, padx=10)

    def control_widgets(self):
        self.loadsongs=tk.Button(self.controls, bg="green", fg="white", font=10)
        self.loadsongs['text']= 'Load Songs'
        self.loadsongs['command']= self.retrieve_songs
        self.loadsongs.grid(row=0, column=0, padx=10)

        self.prev = tk.Button(self.controls, image=prev)
        self.prev['command'] = self.prev_song
        self.prev.grid(row=0, column=0)

        self.pause = tk.Button(self.controls, image=pause)
        self.pause['command'] = self.pause_song
        self.pause.grid(row=0, column=2)

        self.next = tk.Button(self.controls, image=next_)
        self.next['command'] = self.next_song
        self.next.grid(row=0, column=3)

        self.volume = tk.DoubleVar(self)
        self.slider = tk.Scale(self.controls, from_ =0, to = 10, orient= tk.HORIZONTAL)









    




