from tkinter import *
import random
import time
from master_word_list import words

root = Tk()
root.resizable(False, False)
root.geometry("1000x575") #1440x850
root.title('Memory Game')
root.configure(background="#151326")

def user_guessed(clicked):
    global score, lives, current_word

    #If user is correct
    if (current_word in seen_word_list and clicked == 'Seen') or (current_word not in seen_word_list and clicked == 'Not seen'): 
        score += 1
        score_label.configure(text=score)
        green_animation(clicked, True)

    #If user is incorrect
    else: 
        lives -= 1
        lives_label.configure(text=lives)
        if lives == 0:
            user_loses()
            return
        else:
            red_animation(clicked, True)

    if current_word not in seen_word_list:
        seen_word_list.append(current_word) #Add the current word to the seen list unless it's already in it.

    if current_word in master_word_list:
        master_word_list.remove(current_word) #Remove the current word from the master list.

    last_word = current_word

    #New word cannot be the same as the last word
    valid_word = False
    while valid_word == False:
        if random.randint(1,100) > probability_of_repeat or score <= 3:
            current_word = random.choice(master_word_list)
        else:
            current_word = random.choice(seen_word_list)
        
        if last_word != current_word:
            valid_word = True

    current_word_label.place_forget()
    current_word_label.configure(text=current_word.upper())
    current_word_label.place(x=500, y=275, anchor=CENTER)

def user_loses():
    global play_again_button_image, play_again_button, game_over_label, game_over_score_label, game_over_score_descriptor_label, game_over_percentage_label, game_over_percentage_descriptor_label, game_over_lives_label, game_over_lives_descriptor_label

    current_word_label.place_forget()
    lives_label.place_forget()
    lives_descriptor_label.place_forget()
    score_label.place_forget()
    score_descriptor_label.place_forget()
    title_banner_label.place_forget()
    seen_button.place_forget()
    not_seen_button.place_forget()

    game_over_label = Label(root, text='GAME OVER.', bg="#151326", fg="red", font=("Helvetica", 75, "bold"))
    game_over_label.place(x=500, y=80, anchor=CENTER)

    game_over_score_label = Label(root, text=score, bg="#151326", fg="#00a5ec", font=("Helvetica", 75, "bold"))
    game_over_score_label.place(x=150, y=250, anchor=CENTER)

    game_over_score_descriptor_label = Label(root, text='SCORE', bg="#151326", fg="#999999", font=("Helvetica", 17, "bold"))
    game_over_score_descriptor_label.place(x=150, y=325, anchor=CENTER)

    game_over_percentage_label = Label(root, text=str(round(score/(score+starting_lives)*100,1)) + '%', bg="#151326", fg="#00a5ec", font=("Helvetica", 75, "bold"))
    game_over_percentage_label.place(x=500, y=250, anchor=CENTER)

    game_over_percentage_descriptor_label = Label(root, text='PERCENTAGE', bg="#151326", fg="#999999", font=("Helvetica", 17, "bold"))
    game_over_percentage_descriptor_label.place(x=500, y=325, anchor=CENTER)

    game_over_lives_label = Label(root, text=starting_lives, bg="#151326", fg="#00a5ec", font=("Helvetica", 75, "bold"))
    game_over_lives_label.place(x=850, y=250, anchor=CENTER)

    game_over_lives_descriptor_label = Label(root, text='LIVES', bg="#151326", fg="#999999", font=("Helvetica", 17, "bold"))
    game_over_lives_descriptor_label.place(x=850, y=325, anchor=CENTER)

    play_again_button_image = PhotoImage(file="Memory Game Images/play_again.png")
    play_again_button = Button(root, image=play_again_button_image, highlightbackground="#151326", bg='#151326', activebackground='#151326', bd=0, padx=0, pady=0, command=new_game_selected)
    play_again_button.place(x=500, y=500, anchor=CENTER)

def new_game_selected():
    play_again_button.place_forget()
    game_over_label.place_forget()
    game_over_score_label.place_forget()
    game_over_score_descriptor_label.place_forget()
    game_over_percentage_label.place_forget()
    game_over_percentage_descriptor_label.place_forget()
    game_over_lives_label.place_forget()
    game_over_lives_descriptor_label.place_forget()
    start_new_game()

def green_animation(clicked, active):
    if clicked == 'Seen':
        if active == True:
            seen_button.configure(image=correct_seen_button_image)
        elif active == False:
            seen_button.configure(image=seen_button_image)
    elif clicked == 'Not seen':
        if active == True:
            not_seen_button.configure(image=correct_not_seen_button_image)
        elif active == False:
            not_seen_button.configure(image=not_seen_button_image)

    if active == True:
        score_label.configure(fg="#00ff00")
    elif active == False:
        score_label.configure(fg="#00a5ec")
        return

    active = False
    root.after(750, lambda: green_animation(clicked, active))

def red_animation(clicked, active):
    if clicked == 'Seen':
        if active == True:
            seen_button.configure(image=incorrect_seen_button_image)
        elif active == False:
            seen_button.configure(image=seen_button_image)
    elif clicked == 'Not seen':
        if active == True:
            not_seen_button.configure(image=incorrect_not_seen_button_image)
        elif active == False:
            not_seen_button.configure(image=not_seen_button_image)

    if active == True:
        lives_label.configure(fg="#ff0000")
    elif active == False:
        lives_label.configure(fg="#00a5ec")
        return

    active = False
    root.after(750, lambda: red_animation(clicked, active))

def start_new_game():
    global seen_word_list, lives, score, probability_of_repeat, starting_lives, title_banner_image, title_banner_label, lives_label
    global lives_descriptor_label, score_label, score_descriptor_label, current_word, current_word_label, incorrect_seen_button_image, correct_seen_button_image
    global seen_button, seen_button_image, incorrect_not_seen_button_image, correct_not_seen_button_image, not_seen_button_image, not_seen_button, play_again_button, play_again_button_image

    seen_word_list = []
    lives = 3
    score = 0
    probability_of_repeat = 50
    starting_lives = lives

    title_banner_image = PhotoImage(file="Memory Game Images/title_banner.png")
    title_banner_label = Label(root, image=title_banner_image, bg="#151326")
    title_banner_label.pack()
    title_banner_label.place(x=500, y=60, anchor=CENTER)

    lives_label = Label(root, text=lives, bg="#151326", fg="#00a5ec", font=("Helvetica", 60, "bold"))
    lives_label.place(x=10, y=60, anchor=W)

    lives_descriptor_label = Label(root, text='LIVES', bg="#151326", fg="#999999", font=("Helvetica", 15))
    lives_descriptor_label.place(x=10, y=115, anchor=W)

    score_label = Label(root, text=score, bg="#151326", fg="#00a5ec", font=("Helvetica", 60, "bold"))
    score_label.place(x=990, y=60, anchor=E)

    score_descriptor_label = Label(root, text='SCORE', bg="#151326", fg="#999999", font=("Helvetica", 15))
    score_descriptor_label.place(x=990, y=115, anchor=E)

    current_word = random.choice(words)
    current_word_label = Label(root, text=current_word.upper(), bg="#151326", fg="#00a5ec", font=("Helvetica", 70, "bold"))
    current_word_label.place(x=500, y=275, anchor=CENTER)

    incorrect_seen_button_image = PhotoImage(file="Memory Game Images/seen_incorrect.png")
    correct_seen_button_image = PhotoImage(file="Memory Game Images/seen_correct.png")
    seen_button_image = PhotoImage(file="Memory Game Images/seen.png")
    seen_button = Button(root, image=seen_button_image, highlightbackground="#151326", bg='#151326', activebackground='#151326', bd=0, padx=0, pady=0, command=lambda: user_guessed('Seen'))
    seen_button.place(x=300, y=480, anchor=CENTER)

    incorrect_not_seen_button_image = PhotoImage(file="Memory Game Images/not_seen_incorrect.png")
    correct_not_seen_button_image = PhotoImage(file="Memory Game Images/not_seen_correct.png")
    not_seen_button_image = PhotoImage(file="Memory Game Images/not_seen.png")
    not_seen_button = Button(root, image=not_seen_button_image, highlightbackground="#151326", bg='#151326', activebackground='#151326', bd=0, padx=0, pady=0, command=lambda: user_guessed('Not seen'))
    not_seen_button.place(x=700, y=480, anchor=CENTER)

start_new_game()

root.mainloop()