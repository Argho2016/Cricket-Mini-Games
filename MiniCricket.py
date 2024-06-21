import random

def generate_computer_score():
    return random.choice([0, 1, 2, 4, 6])

def calculate_strike_rate(runs, balls):
    if balls == 0:
        return 0.0
    return (runs / balls) * 100

def play_cricket_game():
    total_wickets = 5
    total_balls = 60
    balls_remaining = total_balls
    batsmen = []
    out_count = 0
    
    for i in range(total_wickets):
        batsman_name = input(f"Enter the name of batsman {i + 1}: ")
        runs = 0
        balls_faced = 0

        while balls_remaining > 0:
            player_score = int(input(f"Enter your score for ball {total_balls - balls_remaining + 1} (0, 1, 2, 4, 6): "))
            if player_score not in [0, 1, 2, 4, 6]:
                print("Invalid input! Please enter 0, 1, 2, 4, or 6.")
                continue
            
            balls_faced += 1
            balls_remaining -= 1
            computer_score = generate_computer_score()
            print(f"Computer's score: {computer_score}")

            if player_score == computer_score:
                if player_score == 0 and random.choice([True, False]):
                    print(f"{batsman_name} got out on a 0 with a 50% chance!")
                    break
                else:
                    print(f"{batsman_name} got out!")
                    break
            else:
                runs += player_score
                print(f"{batsman_name} scored {player_score} runs.")

        batsmen.append({
            "name": batsman_name,
            "runs": runs,
            "balls": balls_faced,
            "strike_rate": calculate_strike_rate(runs, balls_faced)
        })
        out_count += 1
        balls_remaining = total_balls

    print("\nAll players are out! Final scoreboard:")
    print("{:<20} {:<10} {:<10} {:<10} {:<10}".format("Batsman", "Runs", "Balls", "Strike Rate", "Total Runs"))
    for batsman in batsmen:
        print("{:<20} {:<10} {:<10} {:<10.2f} {:<10}".format(batsman["name"], batsman["runs"], batsman["balls"], batsman["strike_rate"], batsman["runs"]))

    total_runs = sum(batsman["runs"] for batsman in batsmen)
    total_balls_faced = sum(batsman["balls"] for batsman in batsmen)
    print(f"\nTotal runs scored: {total_runs}")
    print(f"Total balls faced: {total_balls_faced}")

if __name__ == "__main__":
    play_cricket_game()
