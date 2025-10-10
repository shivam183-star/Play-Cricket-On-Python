import random

def user_bat_first(overs, balls, players):
    user_runs = 0
    wickets= 0
    for over in range(overs):
        for ball in range(balls):
            r = int(input(f"Over {over+1}, Ball {ball+1}: \nEnter your run (0-6): "))
            c = random.randint(0, 6)
            print(f"Computer bowled: {c}")
            if r == c:
                print(f"Out! New players comes to bat")
                wickets += 1
                print(f"Score: {user_runs}/{wickets}")
                if wickets == players:
                    print(f"All out at Score {user_runs}/{wickets}")
                    return user_runs
            else:
                user_runs += r
                print(f"You scored {r} runs. Score: {user_runs}/{wickets}")
        print(f"End of Over {over+1}. Score: {user_runs}/{wickets}")
    print(f"Your Innings over! Final Score: {user_runs}/{wickets}.")
    return user_runs

def computer_bat_first(overs, balls, players):
    computer_runs = 0
    wickets = 0
    for over in range(overs):
        for ball in range(balls):
            c = random.randint(0, 6)
            r = int(input(f"Over {over+1}, Ball {ball+1}: \nEnter your bowl (0-6): "))
            print(f"Computer batted: {c}")
            if r == c:
                print(f"Out! Computer's new batsman comes")
                wickets += 1
                print(f"Score: {computer_runs}/{wickets}")
                if wickets == players:
                    print("All out at Score {computer_runs}/{wickets}")
                    return computer_runs
            else:
                computer_runs += c
                print(f"Computer scored {c} runs. Score: {computer_runs}/{wickets}")
        print(f"End of Over {over+1}. Score: {computer_runs}/{wickets}")
    print(f"Computer Innings over! Final Score: {computer_runs}/{wickets}.")
    return computer_runs

def user_chase(target, overs, balls, players):
    user_runs = 0
    wickets = 0
    for over in range(overs):
        for ball in range(balls):
            r = int(input(f"Over {over+1}, Ball {ball+1}: \nEnter your run (0-6): "))
            c = random.randint(0, 6)
            print(f"Computer bowled: {c}")
            if r == c:
                print(f"Out! New players comes to bat")
                wickets += 1
                print(f"Score: {user_runs}/{wickets}")
                if wickets == players:
                    print(f"All out at Score {user_runs}/{wickets} You lost the game")
                    print(f"Computer won by {target - user_runs-1} runs")
                    break
            else:
                user_runs += r
                print(f"You scored {r} runs. Score: {user_runs}/{wickets}")
                if user_runs >= target:
                    print(f"You have chased down the target! You won by {players- wickets} wickets")
                    break
        print(f"End of Over {over+1}. Score: {user_runs}/{wickets}")
    if user_runs < target:
        print(f"You couldn't chase the target. Computer won by {target - user_runs-1} runs")
    if user_runs == target:
        print("Match Drawn")
    print(f"Final Score: {user_runs}/{wickets}.")

def computer_chase(target, overs, balls, players):
    computer_runs = 0
    wickets = 0
    for over in range(overs):
        for ball in range(balls):
            c = random.randint(0, 6)
            r = int(input(f"Over {over+1}, Ball {ball+1}: \nEnter your bowl (0-6): "))
            print(f"Computer batted: {c}")
            if r == c:
                print(f"Out! Computer's new batsman comes")
                wickets += 1
                print(f"Score: {computer_runs}/{wickets}")
                if wickets == players:
                    print(f"All out at Score {computer_runs}/{wickets}. You won by {target - computer_runs-1} runs")
                    break
            else:
                computer_runs += c
                print(f"Computer scored {c} runs. Score: {computer_runs}/{wickets}")
                if computer_runs >= target:
                    print(f"Computer has chased down the target! Computer won by {players- wickets} wickets")
                    break
        print(f"End of Over {over+1}. Score: {computer_runs}/{wickets}")
    if computer_runs < target:
        print(f"Computer couldn't chase the target. You won by {target - computer_runs-1} runs")
    if computer_runs == target:
        print("Match Drawn")
    print(f"Final Score: {computer_runs}/{wickets}.")

if __name__ == "__main__":
   print("Cricket game You vs Computer")
overs = int(input("Enter number of overs: "))
balls = 6
players = int(input("Enter number of players in a team: "))

user_runs = 0
computer_runs = 0
user_wickets = players
computer_wickets = players
target = 0
print("Toss time! Choose Heads or Tails")
toss = input("Enter your choice: ").lower()
toss_result = random.choice(["heads", "tails"])
if toss == toss_result:
    print("You won the toss! Choose to bat or bowl first")
    choice = input("Enter your choice: ").lower()
    if choice == "bat":
        batting_first = "user"
    else:
        batting_first = "computer"
else:
    choice = random.choice(["heads", "tails"])
    print(f"Computer won the toss! chooses to {choice} first")
    if choice == "bat":
        batting_first = "Computer"
    else:
        batting_first = "user"

if batting_first == "user":
    user_runs = user_bat_first(overs, balls, players)
    target = user_runs + 1
    print(f"Computer needs {target} runs to win")
    computer_chase(target, overs, balls, players)
else:
    computer_runs = computer_bat_first(overs, balls, players)
    target = computer_runs + 1
    print(f"You need {target} runs to win")
    user_chase(target, overs, balls, players)