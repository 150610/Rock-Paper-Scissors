# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans =("yes", "no")):

    error = f"Please enter a valid response from the following list: {valid_ans}"

    while True:

        # get user response and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            #check if the user response is in the word list
            if item == user_response:
                return item

            #check if the user response is the same as the
            # #first letter of an item in the list
            elif user_response == item[0]:
                return item

        #print error if the user does not enter a valid response
        print(error)
        print()


# displays instructions
def instructions():
    """Prints instructions"""

    print("""
    *** Instructions ****

To begin, chose the number of rounds you want to play.
(Or play infinite mode).

Then vs the computer. You have to play R (rock), P (paper), or S (scissors).

The rules are:
  .  Paper beats rock
  .  Rock beats scissors 
  .  Scissors beats paper

Press <xxx> to end the game at anytime. 

Good Luck!

    """)


# checks for an integer more than / equal to 1
def int_check(question):
    while True:
        error = "Please enter an integer more than / equal to 1"

        to_check = input(question)

        # check for infinite mode
        if to_check =="":
            return "infinite"

        try:
            response = int(to_check)

            #checks that the number is more than/equal to 1
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# Main routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print("🪨🧻✂️ Rock, Paper, Scissors Game 🪨🧻✂️")
print()

# ask the user if they want instructions (check they say yes/no)
want_instructions = string_checker("Do you want to see the instructions?: ")

#Display the instructions if the user wants to see them
if want_instructions == "yes":
    instructions()

# Ask the user for the number of rounds/infinite mode
num_rounds = int_check("How many rounds would you like to play? Press <enter> for infinite mode: ")

if num_rounds =="infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played +1} (Infinite Mode)"
    else:
        rounds_heading = f"\n Round {rounds_played +1} of {num_rounds}"

    print(rounds_heading)
    print()

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

    # if user choice is the exit code, break the loop
    if user_choice =="xxx":
        break

    rounds_played +=1


    # if users are in infinite mode add more rounds
    if mode == "infinite":
        num_rounds += 1



# Game history/ statistics area