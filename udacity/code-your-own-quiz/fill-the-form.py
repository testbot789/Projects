
to_be_changed = ["___1___", "___2___", "___3___", "___4___"]
correct_answers = ["world", "Python", "print", "HTML"]

easy_string = (''''+++Easy+++Hello ___1___!'  In ___2___ this is particularly easy; all you have to do is type in: ___3____ "Hello ___1___!"
                Of course, that isn't a very useful thing to do. However, it is an
                example of how to output to the user using the ___3___ command, and
                produces a program which does something, so it is useful in that capacity.
                It may seem a bit odd to do something in a Turing complete language that
                can be done even more easily with an ___4___ file in a browser, but it's
                a step in learning ___2___ syntax, and that's really its purpose.''')
medium_string = ('''+++Medium+++Hello ___1___!'  In ___2___ this is particularly easy; all you have to do is type in: ___3____ "Hello ___1___!"
                Of course, that isn't a very useful thing to do. However, it is an
                example of how to output to the user using the ___3___ command, and
                produces a program which does something, so it is useful in that capacity.
                It may seem a bit odd to do something in a Turing complete language that
                can be done even more easily with an ___4___ file in a browser, but it's
                a step in learning ___2___ syntax, and that's really its purpose.''')
hard_string = ('''+++Hard+++Hello ___1___!'  In ___2___ this is particularly easy; all you have to do is type in: ___3____ "Hello ___1___!"
                Of course, that isn't a very useful thing to do. However, it is an
                example of how to output to the user using the ___3___ command, and
                produces a program which does something, so it is useful in that capacity.
                It may seem a bit odd to do something in a Turing complete language that
                can be done even more easily with an ___4___ file in a browser, but it's
                a step in learning ___2___ syntax, and that's really its purpose.''')




def find_word(word, to_be_changed):
    for i in to_be_changed:
        if i in word:
            result = i
            to_be_changed.remove(i)
            return result
    return None
    #This function searches for word in the list to_be_changed, return result and delete word from the list

def show_string(string):
    string = " ".join(string)
    print string
    #This function shows the string in proper way

def check_replacement(string, user_input):
    for word in string:
        replacement = find_word(word, to_be_changed)
        if replacement is not None:
            print "----this is" + replacement
            string = [word.replace(replacement, user_input) for word in string]
            # https://stackoverflow.com/questions/3136689/find-and-replace-string-values-in-python-list
            show_string(string)
            return string
        #check_replacement check if the word in string matched with the word in to_be_changed if so
        # function replaces this word with the user input

def play_game(answers, string):
    remain_try = 5
    question_number = 1
    answer_number = 0
    string = string.split()
    show_string(string)
    while question_number < 5 :
        user_input = raw_input("Please type your answer for ___" + str(question_number) + "___ question: ")
        if user_input == answers[answer_number]:
            check_replacement(string, user_input)
            question_number = question_number + 1
            answer_number = answer_number + 1
        else:
            print ("Wrong answer, you have " + str(remain_try) + " more trys")
            remain_try = remain_try - 1
            if remain_try == 0 :
                print "Game over"
                return
        #in function play_game we make a counter while , get the user_input, if user_input
        #matches with the answer in list we  start check_replacement function and increase counter
        #If the answer is wrong we count the remain tries

selection = raw_input("Please type easy/ medium/ hard :")

def select_difficulty():
    print "Please select a difficulty level from easy/ medium/ hard "
    if selection == "easy":
        print "easy is choosen"
    elif selection == "medium":
        print "medium is choosen"
    elif selection == "hard":
        print "hard is choosen"
    else:
        raise ValueError('input error')
    return selection
# function select_difficulty() asks user to select the difficulty level from (easy/medium/hard)
# if user types incorrect, functioun will throw an errow

def first_blank(selection):
    if selection == "easy":
        play_game(correct_answers, easy_string)
    elif selection == "medium":
        play_game(correct_answers, medium_string)
    else:
        play_game(correct_answers, hard_string)
    return
#first_blank brings us to the function play game with the choosen level difficulty


select_difficulty()
first_blank(selection)