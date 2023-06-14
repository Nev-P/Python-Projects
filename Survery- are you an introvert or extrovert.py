# Inputs
def surveystart():
    your_name = input("PLEASE INPUT YOUR NAME >> ")
    your_name = input("hello, " + your_name + "! Press enter to continue >>")
    user_answer = int()
    user_answer_one = int()
    user_answer_two = int()
    user_answer_three = int()
    user_answer_four = int()
    user_answer_five = int()
    user_answer_six = int()
    user_answer_seven = int()
    user_answer_eight = int()
    user_answer_nine = int()
    total_const = 0
# Natasha & Nevaeh

# Nevaeh & Natasha
# Intro
# Loops after it is finished

    def Introduction():
        print("==================================================")
        print("This is a psychological assessment survey. You will be asked 10 questions.")
        print("The purpose of these questions is to evaluate your personality traits in order to categorize you into either being an extrovert or introvert.")
        print("For each question type in a number from 0 to 5.")
        print("Any number from 0-2 would be something you are unlikely to do, and 3-5 is something you are most likely to do.")
        print("Alright, let's start!")
        print("==================================================")

    Introduction()

# Natasha & Nevaeh
    def addTenNumbers(user_answer, user_answer_one, user_answer_two, user_answer_three, user_answer_four, user_answer_five,
                    user_answer_six, user_answer_seven, user_answer_eight, user_answer_nine):
    # Questions: 1 to 10
    ### Introversion Questions
    ##Question 1
        print("When you are with friends or people you just met, are you the one to be more outspoken and start a conversation? >>")
        user_answer = input("Please enter your answer >> ")
        while not user_answer.isnumeric() or (int(user_answer) < 0 or int(user_answer) > 5):
            user_answer = input("Please enter a valid number (0-5) Any number from 0-2 would be something you are unlikely to do, and 3-5 is something you are most likely to do >> ")
    ##Question 2
        print("It is the weekend, are you most likely to be by yourself at home, doing something you like? >>")
        user_answer_one = input("Please enter your answer >>")
        while not user_answer_one.isnumeric() or (int(user_answer_one) < 0 or int(user_answer_one) > 5):
            user_answer_one = input("Please enter a valid number (0-5) Any number from 0-2 would be something you are unlikely to do, and 3-5 is something you are most likely to do >> ")
    ##Question 3
        print("There is someone you like, are you most likely to ask them out first? >> ")
        user_answer_two = input("Please enter your answer >>")
        while not user_answer_two.isnumeric() or (int(user_answer_two) < 0 or int(user_answer_two) > 5):
            user_answer_two = input("Please enter a valid number (0-5) Any number from 0-2 would be something you are unlikely to do, and 3-5 is something you are most likely to do >> ")
    ##Question 4
        print("Would your relatives and close friends say you are mostly quiet than outspoken? >> ")
        user_answer_three = input("Please enter your answer >>")
        while not user_answer_three.isnumeric() or (int(user_answer_three) < 0 or int(user_answer_three) > 5):
            user_answer_three = input("Please enter a valid number (0-5) Any number from 0-2 would be something you are unlikely to do, and 3-5 is something you are most likely to do >> ")
    ##Question 5
        print("Do you sometimes find your energy drained after hanging out around people? >> ")
        user_answer_four = input("Please enter your answer >>")
        while not user_answer_four.isnumeric() or (int(user_answer_four) < 0 or int(user_answer_four) > 5):
            user_answer_four = input("Please enter a valid number (0-5) Any number from 0-2 would be something you are unlikely to do, and 3-5 is something you are most likely to do >> ")
    ### Extroversion Questions
    ##Question 6
        print("Is it likely for you to be assertive when speaking to someone you do not know? >> ")
        user_answer_five = input("Please enter your answer >>")
        while not user_answer_five.isnumeric() or (int(user_answer_five) < 0 or int(user_answer_five) > 5):
            user_answer_five = input("Please enter a valid number (0-5) Any number from 0-2 would be something you are unlikely to do, and 3-5 is something you are most likely to do >> ")
    ##Question 7
        print("Is it likely for you to voice your emotions to people you do not know? >> ")
        user_answer_six = input("Please enter your answer >>")
        while not user_answer_six.isnumeric() or (int(user_answer_six) < 0 or int(user_answer_six) > 5):
            user_answer_six = input("Please enter a valid number (0-5) Any number from 0-2 would be something you are unlikely to do, and 3-5 is something you are most likely to do >> ")
    ##Question 8
        print("Is it likely for you to have high amounts of energy around people you just met? >> ")
        user_answer_seven = input("Please enter your answer >>")
        while not user_answer_seven.isnumeric() or (int(user_answer_seven) < 0 or int(user_answer_seven) > 5):
            user_answer_seven = input("Please enter a valid number (0-5) Any number from 0-2 would be something you are unlikely to do, and 3-5 is something you are most likely to do >> ")
    ##Question 9
        print("Is it likely for you to become nervous and less outspoken when meeting new people? >> ")
        user_answer_eight = input("Please enter your answer >>")
        while not user_answer_eight.isnumeric() or (int(user_answer_eight) < 0 or int(user_answer_eight) > 5):
            user_answer_eight = input("Please enter a valid number (0-5) Any number from 0-2 would be something you are unlikely to do, and 3-5 is something you are most likely to do >> ")
    ##Question 10
        print("Is it likely for you to live in a busy city? >> ")
        user_answer_nine = input("Please enter your answer >>")
        while not user_answer_nine.isnumeric() or (int(user_answer_nine) < 0 or int(user_answer_nine) > 5):
            user_answer_nine = input("Please enter a valid number (0-5) Any number from 0-2 would be something you are unlikely to do, and 3-5 is something you are most likely to do >> ")

        sum = int(user_answer) + int(user_answer_one) + int(user_answer_two) + int(user_answer_three) + int(user_answer_four) + int(user_answer_five) + int(user_answer_six) + int(user_answer_seven) + int(user_answer_eight) + int(user_answer_nine)
        return sum


    total_const = addTenNumbers(user_answer, user_answer_one, user_answer_two, user_answer_three, user_answer_four, user_answer_five,
                user_answer_six, user_answer_seven, user_answer_eight, user_answer_nine)

# Nevaeh & Natasha
#results
    def results(TotalAmount):
        if TotalAmount < 30:
            print("Your score is:" + str((TotalAmount)) + " According to your results: You are an introvert")
        elif TotalAmount > 30:
            print("Your score is:" + str((TotalAmount)) + " According to your results: You are an extrovert")
        else:
            TotalAmount = 30
            print("Your score is:" + str((TotalAmount)) + " You are both an introvert and extrovert")

    results(total_const)

    reset = input("Do you want to play again? Type 'y' for yes or 'n' for no >> ")
    if reset == "Y" or reset == "y":
        surveystart()

surveystart()

