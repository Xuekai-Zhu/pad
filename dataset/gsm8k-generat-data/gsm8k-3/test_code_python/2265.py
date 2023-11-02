def solution():
    """There were 50 racers in a bicycle charity race at the beginning of the race. After 20 minutes, 30 more racers joined the race. The total number of racers doubled after another 30 minutes. If at the end of the race only 130 people finished the race, what's the total number of people who dropped before finishing the race?"""
    # Define the initial number of racers
    initial_racers = 50

    # Calculate the number of racers after 20 minutes
    racers_after_20_mins = initial_racers + 30

    # Calculate the number of racers after 50 minutes (30 minutes after the initial 20 minutes)
    racers_after_50_mins = racers_after_20_mins * 2

    # Calculate the number of racers who dropped out before finishing
    racers_dropped_out = racers_after_50_mins - 130

    # Display the number of racers who dropped out
    result = racers_dropped_out
    return result

print(solution())