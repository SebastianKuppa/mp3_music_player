from pygame import mixer
import os
import tkinter
import tkinter.font as font
from tkinter import filedialog


def add_songs():
    temp_song = filedialog.askopenfilename(initialdir='/', title='Choose a song..', filetypes=(('mp3 files', '*.mp3'),))
    # for s in temp_song:
    #     s.replace()


def delete_songs():
    curr_song = songs_list.curselection()
    songs_list.delete(curr_song[0])


def play_song():
    song = songs_list.get(tkinter.ACTIVE)
    mixer.music.load(song)
    mixer.music.play()


def pause_song():
    mixer.music.pause()


def stop_song():
    mixer.music.stop()
    songs_list.selection_clear(tkinter.ACTIVE)


def resume_song():
    mixer.music.unpause()


def prev_song():
    previous_song = songs_list.curselection()[0] - 1
    temp2 = songs_list.get(previous_song)
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0, tkinter.END)
    songs_list.activate(previous_song)
    songs_list.selection_set(previous_song)


def next_song():
    following_song = songs_list.curselection()[0] + 1
    temp2 = songs_list.get(following_song)
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0, tkinter.END)
    songs_list.activate(following_song)
    songs_list.selection_set(following_song)


if __name__ == '__main__':
    # creating root window
    root = tkinter.Tk()
    root.title('MP3 music player')
    # init mixer
    mixer.init()
    # init listbox for playlist
    songs_list = tkinter.Listbox(root, selectmode=tkinter.SINGLE, bg="black", fg="white", font=('arial', 15), height=12, width=47,
                                 selectbackground="gray", selectforeground="black")
    songs_list.grid(columnspan=9)
    # font for the music player
    custom_font = tkinter.font.Font(family='Helvetica')
    # init play button
    play_button = tkinter.Button(master=root, text='PLAY', width=7, command=play_song)
    play_button['font'] = custom_font
    play_button.grid(row=1, column=0)
    # init pause button
    pause_button = tkinter.Button(master=root, text='PAUSE', width=7, command=pause_song)
    pause_button['font'] = custom_font
    pause_button.grid(row=1, column=1)
    # init stop button
    stop_button = tkinter.Button(master=root, text='STOP', width=7, command=stop_song)
    stop_button['font'] = custom_font
    stop_button.grid(row=1, column=2)
    # init resume button
    resume_button = tkinter.Button(master=root, text='RESUME', width=7, command=resume_song)
    resume_button['font'] = custom_font
    resume_button.grid(row=1, column=3)
    # init previous button
    prev_button = tkinter.Button(master=root, text='PREV', width=7, command=prev_song)
    prev_button['font'] = custom_font
    prev_button.grid(row=1, column=4)
    # init next button
    prev_button = tkinter.Button(master=root, text='NEXT', width=7, command=next_song)
    prev_button['font'] = custom_font
    prev_button.grid(row=1, column=5)

    # init menu
    my_menu = tkinter.Menu(master=root)
    root.config(menu=my_menu)
    add_song_menu = tkinter.Menu(my_menu)
    my_menu.add_cascade(label='Menu', menu=add_song_menu)
    add_song_menu.add_command(label='Add songs', command=add_songs)
    add_song_menu.add_command(label='Delete songs', command=delete_songs)

    tkinter.mainloop()
