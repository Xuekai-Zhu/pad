def solution():
    # Define the starting number of balls and the frequency of events that affect the number of balls
    starting_balls = 2
    worn_out_frequency = 10
    lost_frequency = 5
    new_canister_frequency = 4

    # Calculate the number of balls worn out, lost, and gained from canisters
    balls_worn_out = (20 // worn_out_frequency)
    balls_lost = (20 // lost_frequency)
    canisters_bought = (20 // new_canister_frequency)
    balls_gained = (canisters_bought * 3)

    # Calculate the final number of balls
    final_balls = starting_balls - 1 + balls_gained - balls_worn_out - balls_lost
    result = final_balls
    return result

print(solution())