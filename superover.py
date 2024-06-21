import random

def bowl_ball():
    outcomes = [0, 1, 2, 3, 4, 6, 'W']
    return random.choice(outcomes)

def play_cricket():
    print("Welcome to the Superover Cricket Game!")
    print("You have 1 over (6 balls) to score as many runs as you can.")
    print("If you get 'W' (wicket), you're out.")
    
    total_runs = 0
    balls_left = 6

    while balls_left > 0:
        input("Press Enter to face the next ball...")
        outcome = bowl_ball()
        
        if outcome == 'W':
            print(f"Ball {6 - balls_left + 1}: You got out! Total runs: {total_runs}")
            break
        else:
            print(f"Ball {6 - balls_left + 1}: You scored {outcome} run(s).")
            total_runs += outcome
            balls_left -= 1

    if balls_left == 0:
        print(f"End of the over. Total runs scored: {total_runs}")

if __name__ == "__main__":
    play_cricket()
