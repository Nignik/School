import random
from library_history import library
import os

player_answer = ""
right_answer = ""
question = ""
question1 = ""
question2 = ""
score = 0
max_score = 0


def check_answer_easy(question1, question2, player_answer):
    answer1 = int(library[question1])
    answer2 = int(library[question2])
    global score
    global max_score
    if player_answer == "p":
        if answer1 > answer2:
            score += 1
            max_score = max(score, max_score)
            print(f"Odpowiedz poprawna: {answer1} > {answer2}\nWynik: {score}\n")

        elif answer1 < answer2:
            print(f"Odpowiedz nie poprawna: {answer1} < {answer2}\nNajlepszy wynik: {max_score}\n")
            score = 0

    elif player_answer == "w":
        if answer1 < answer2:
            score += 1
            max_score = max(score, max_score)
            print(f"Odpowiedz poprawna: {answer1} < {answer2}\nWynik: {score}\n")

        elif answer1 > answer2:
            print(f"Odpowiedz nie poprawna: {answer1} > {answer2}\nNajlepszy wynik: {max_score}\n")
            score = 0

    elif player_answer != "koniec":
        print("Nielegalny input")


def check_answer_hard(player_answer, right_answer):
    global score
    global max_score
    if player_answer == right_answer:
        score += 1
        max_score = max(score, max_score)
        print("Odpowiedz poprawna\n")

    else:
        print(f"Odpowiedz nieprawidlowa. Prawdilowa odpowiedz to: {right_answer}\nWynik: {score}, Rekord: {max_score}")
        score = 0


play = input("Chcesz grac na easy czy hard? 'e' albo 'h': ")

while play != "0":

    if player_answer == "koniec":
        play = input("Chcesz grac na easy czy hard? 'e' albo 'h': ")
        player_answer = ""

    while player_answer != "koniec":
        if play == "h":
            question = random.choice(list(library.keys()))
            right_answer = library[question]
            if question == "Pi" or question == "e":
                player_answer = input(f"Podaj 15 cyfr liczby {question} po przecinku.\n")
            else:
                player_answer = input(f"Kiedy wydarzylo sie: {question}?\n")
            check_answer_hard(player_answer, right_answer)

        elif play == "e":
            question1 = random.choice(list(library.keys()))
            answer1 = library[question1]
            question2 = random.choice(list(library.keys()))
            while question1 == question2 or question1 == "Pi" or question2 == "Pi" or question1 == "e" or question2 == "e":
                question2 = random.choice(list(library.keys()))
            player_answer = input(
                f"Czy {question1}-{answer1} wydarzylo sie wczesniej od {question2}: 'w', czy pozniej: 'p'?\n")
            check_answer_easy(question1, question2, player_answer)
