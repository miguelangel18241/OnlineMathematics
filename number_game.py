import random
import inflect
from termcolor import colored, cprint
import time


def wrong_answer():
    print("Mmm... I don't think so...\n")
    print(f'The correct answer is: {result}')
    print("See you next time...\n")
    print(f'In total {players_name} accumulated {score} points!\n')
    print("GOOD LUCK NEXT TIME\n")
    is_correct = False


def congratulations_message():
    random_number = random.randint(1, 9)
    if random_number == 1:
        print("WELL DONE!!!\n")
    elif random_number == 2:
        print("NICELY DONE!!!\n")
    elif random_number == 3:
        print("KEEP IT UP!!!\n")
    elif random_number == 4:
        print("YOU ARE A MATH GENIUS!!!\n")
    elif random_number == 5:
        print("IMPRESSVE!!!\n")
    elif random_number == 6:
        print("WHO SAID MATHEMATICS ARE BORING? GOOD JOB\n")
    elif random_number == 7:
        print("CONGRATULATIONS!!!\n")
    elif random_number == 8:
        print("SUPER NICE!!!\n")
    else:
        print("AMAZING\n")


def easy_mathematical_operation():
    number_one = random.randint(1, 9)
    number_two = random.randint(1, 9)
    random_number = random.randint(1, 3)
    result = 0
    if random_number == 1:
        # sum
        result = number_one + number_two
        print(
            f'What is the result of the following maths problem:\n{number_one} + {number_two} ? \n')
    elif random_number == 2:
        # substract
        result = number_one - number_two
        print(
            f'What is the result of the following maths problem:\n{number_one} - {number_two} ? \n')
    else:
        # multiply
        result = number_one * number_two
        print(
            f'What is the result of the following maths problem:\n{number_one} * {number_two} ? \n')
    return result


def hard_mathematical_operation():
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    random_number = random.randint(1, 3)
    result = 0
    if random_number == 1:
        # sum
        result = number_one + number_two
        print(
            f'What is the result of the following maths problem:\n{number_one} + {number_two} ? \n')
    elif random_number == 2:
        # substract
        result = number_one - number_two
        print(
            f'What is the result of the following maths problem:\n{number_one} - {number_two} ?\n ')
    else:
        # multiply
        result = number_one * number_two
        print(
            f'What is the result of the following maths problem:\n{number_one} * {number_two} ? \n')
    return result


print("♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡")
cprint('♡ ♡ ♡ ♡ ♡       WELCOME TO ONLINE MATHEMATICS      ♡ ♡ ♡ ♡ ♡ ',
       'white', attrs=['blink'])
print("♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡")
print(" ♡ IN THIS GAME YOU GET ONE POINT FOR EVERY CORRECT ANSWER ♡ ")
print("♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡\n")
# Main Function
while True:
    try:
        number_of_players = int(input("How many players today?\n"))
        break
    except ValueError:
        print("Please enter a valid number.\n")
total_scores = []
# p = inflect.engine()
for x in range(number_of_players):
    print("Nickname?")
    players_name = input()
    print("\n")
    print(f'Hello {players_name}, thank you for playing!\n')
    score = 0
    is_correct = True
    while is_correct == True:
        if score < 5:
            start_time = time.time()
            result = easy_mathematical_operation()
            player_result = int(input())
            if player_result == result:
                score = score + 1
                congratulations_message()
                is_correct = True
                if score == 1:
                    print(f'So far you have earned {score} point\n')
                else:
                    print(f'So far you have earned {score} points\n')
            else:
                wrong_answer()
                is_correct = False
                break
        else:
            result = hard_mathematical_operation()
            player_result = int(input())
            if player_result == result:
                score = score + 1
                congratulations_message()
                is_correct = True
                if score == 1:
                    print(f'So far you have earned {score} point\n')
                else:
                    print(f'So far you have earned {score} points')
            else:
                wrong_answer()
                is_correct = False
                break
    finish_time = time.time()
    duration = finish_time - start_time

    total_scores.append([score, players_name, duration])


# print("User took", duration, "seconds to input something.")

total_scores.sort(reverse=True)

# max = total_scores.index(max(total_scores))
# winners_score = total_scores[max][0]
# winners_name = total_scores[max][1]


cprint(f'The winner is {total_scores[0][1]} with a total of {total_scores[0][0]} points\n',
       'white', attrs=['blink'])
print(
    f'CONGRATULATIONS {total_scores[0][1]}, the time it took you to get the right answer was {round(total_scores[0][2],2)} seconds\n')

print("OTHER SCORES:\n")

total_scores.sort(reverse=True)
for i in range(len(total_scores)-1):
    print(
        f'Position {i+2}: with {total_scores[i+1][0]} points\n - {total_scores[i+1][1]} with a duration of {round(total_scores[i+1][2],2)} seconds')
