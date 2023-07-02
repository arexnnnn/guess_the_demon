# This is a simple program to guess the correct demon in the Demon Slayer anime
# You can guess the answer in lowercase format
# Just a beginner program to clear up the basics
# I also learned how to add projects to github using pycharm, its almost the same process

print("Which upper moon holds the 3rd spot in Demon Slayer anime?")
secret_word = "akaza"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("Correct guess, YOU WIN!")