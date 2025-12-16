import random

def get_input(run):
    try:
        r = int(input(run))
        if 0 <= r <= 6:
            return r
        else:
            print("Enter number between 0 and 6")
            return None
    except ValueError:
        print("Invalid input! Enter a number.")
        return None


def user_bat(overs, balls, players):
    runs = wickets = 0
    for over in range(overs):
        for ball in range(balls):
            r = get_input(f"Over {over+1} Ball {ball+1} \nYour run: ")
            if r is None:
                continue

            c = random.randint(0, 6)
            print("Computer bowled:", c)

            if r == c:
                wickets += 1
                print(f"OUT! Score: {runs}/{wickets}")
                if wickets == players:
                    return runs
            else:
                runs += r
                print(f"Score: {runs}/{wickets}")
        print(f"End of over {over+1}: {runs}/{wickets}")
    return runs


def computer_bat(overs, balls, players):
    runs = wickets = 0
    for over in range(overs):
        for ball in range(balls):
            r = get_input(f"Over {over+1} Ball {ball+1} \nYour bowl: ")
            if r is None:
                continue

            c = random.randint(0, 6)
            print("Computer played:", c)

            if r == c:
                wickets += 1
                print(f"OUT! Score: {runs}/{wickets}")
                if wickets == players:
                    return runs
            else:
                runs += c
                print(f"Score: {runs}/{wickets}")
        print(f"End of over {over+1}: {runs}/{wickets}")
    return runs


def user_chase(target, overs, balls, players):
    runs = wickets = 0
    for over in range(overs):
        for ball in range(balls):
            r = get_input(f"Over {over+1} Ball {ball+1} \nYour run: ")
            if r is None:
                continue

            c = random.randint(0, 6)
            print("Computer bowled:", c)

            if r == c:
                wickets += 1
                print(f"OUT! Score: {runs}/{wickets}")
                if wickets == players:
                    return False
            else:
                runs += r
                if runs >= target:
                    return True
        print(f"End of over {over+1}: {runs}/{wickets}")
    return False


def computer_chase(target, overs, balls, players):
    runs = wickets = 0
    for over in range(overs):
        for ball in range(balls):
            r = get_input(f"Over {over+1} Ball {ball+1} \nYour bowl: ")
            if r is None:
                continue

            c = random.randint(0, 6)
            print("Computer played:", c)

            if r == c:
                wickets += 1
                print(f"OUT! Score: {runs}/{wickets}")
                if wickets == players:
                    return True
            else:
                runs += c
                if runs >= target:
                    return False
        print(f"End of over {over+1}: {runs}/{wickets}")
    return True


if __name__ == "__main__":
    print("Python Cricket: You vs Computer")

    overs = int(input("Enter overs: "))
    players = int(input("Enter players per team: "))
    balls = 6

    toss = input("Toss (heads/tails): ").lower()
    toss_result = random.choice(["heads", "tails"])

    if toss == toss_result:
        choice = input("You won toss! Bat or bowl? ").lower()
        batting_first = "user" if choice == "bat" else "computer"
    else:
        batting_first = random.choice(["user", "computer"])
        print("Computer won toss!")

    if batting_first == "user":
        user_score = user_bat(overs, balls, players)
        print("Target:", user_score + 1)
        result = computer_chase(user_score + 1, overs, balls, players)
        print("You win!" if result else "Computer wins!")
    else:
        comp_score = computer_bat(overs, balls, players)
        print("Target:", comp_score + 1)
        result = user_chase(comp_score + 1, overs, balls, players)
        print("You win!" if result else "Computer wins!")
