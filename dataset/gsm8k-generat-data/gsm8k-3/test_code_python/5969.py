def solution():
    """Candace decides to enter a race. The race is run in 4 segments, with racers eliminated at the end of each segment. 10 racers are eliminated after the first segment. A third of the remaining racers are eliminated after the next section. Half of the remaining racers are eliminated before the last leg of the race. If 100 racers started the race, how many will run in the final section of the race?"""
    # Define the starting number of racers
    starting_racers = 100

    # Calculate the number of racers remaining after each segment and update the variable
    remaining_racers = starting_racers - 10
    remaining_racers //= 3
    remaining_racers *= 2

    # Display the number of racers remaining for the final segment
    result = remaining_racers
    return result

print(solution())