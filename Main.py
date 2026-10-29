#A quiz about the game Wizard101
def intro(name):
    print()
    print("Welcome to my Wizard101 Quiz,", name + "!")
    print("Today you will be tested on knowledge about Wizard101.")
name = input("What's your name? ")
def rules():
    print()
    print("Quiz rules:")
    print("1. Type answer, and then press ENTER")
    print("2. spelling DOES matter")
    print("3. Answers are not case sensitive")
    print("4. Read each question carefully before answering")
    print("5. Each correct answer will give you 1 point")
    print("6. There are a total of 10 questions")
    print("7. Do not add extra punctuation to your answers")
    print("8. Use full names when the question asks for a name")
    print("9. You may replay the quiz after finishing")
    print()
def starting():
    print("You will be tested in:")
    for number in range(3, 0, -1):
        print(number)
    print("begin.")
    print()
def asking_question(question_number, question, right_answer):
    print("Question", question_number, "of 10")
    answer = input(question).lower()

    if answer == right_answer:
        print("Correct")
        print("Nice job!")
        return True
    else:
        print("Incorrect")
        print("The correct answer was", right_answer)
        return False
def play_quiz():
    score = 0

    score += asking_question(1, "Which school's oni spell gambits 4 harmful charms on the opponent for additional damage? ", "storm")
    score += asking_question(2, "Who is the main antagonist of the Crying Sky Raid? ", "hunhau")
    score += asking_question(3, "What hanging effect is gambited on the path B Sunbird to do 335 extra base damage? ", "dot")
    score += asking_question(4, "Which area houses a series of dungeons ending in the player defeating a shadow version of Malistaire the Undying? ", "castle darkmoor")
    score += asking_question(5, "'Primordial' is the fire school adjective for which gear set? ", "aeon")
    score += asking_question(6, "Who is the librarian found in the Arcanum? ", "fitzhume")
    score += asking_question(7, "Which boss at the end of arc 2 dropped a now retired athame and amulet that was the best for its level? ", "morganthe")
    score += asking_question(8, "What is the name of the best guild ever created? ", "fierce rogue kittens")
    score += asking_question(9, "What world is the ending of the first arc? ", "dragonspyre")
    score += asking_question(10, "What is the first raid to be introduced to the game? ", "voracious void")

    print()
    print("You got", score, "out of 10 questions correct.")

    score_percent = score / 10 * 100
    print("Your score is", score_percent, "%")
    if score == 10:
        print("Amazing!")
        print("You got a perfect score!")
    else:
        print("You did not get a perfect score.")
        if score >= 6:
            print("Good job!")
        elif score >= 4:
            print("Not bad!")
        else:
            print("Do you even play?!")
def ending():
    print()
    print("Thank you for playing the Wizard101 Quiz!")
    print("Your results have been recorded for this attempt.")
    print("You can replay the quiz if you want to try for a better score.")
    print()
intro(name)
rules()
ready = input("Are you ready to start? y/n: ").lower()
while ready not in ("y", "n"):
    print("Error. Please enter y or n.")
    ready = input("Are you ready to start? y/n: ").lower()
while ready == "n":
    print("Take your time.")
    ready = input("Are you ready now? y/n: ").lower()
    while ready not in ("y", "n"):
        print("Error. Please enter y or n.")
        ready = input("Are you ready now? y/n: ").lower()
if ready == "y":
    print("Good luck!")
starting()
play_quiz()
repeat = input("Do you want to play again? y/n: ").lower()
while repeat not in ("y", "n"):
    print("Error. Please enter y or n.")
    repeat = input("Do you want to play again? y/n: ").lower()
while repeat == "y":
    print("Get ready to take the quiz again!")
    starting()
    play_quiz()
    repeat = input("Do you want to play again? y/n: ").lower()
    while repeat not in ("y", "n"):
        print("Error. Please enter y or n.")
        repeat = input("Do you want to play again? y/n: ").lower()
if repeat == "n":
    print("Have a good day!")
    ending()
    input("press ENTER to exit.")
