def solution():
    """Billy and Margaret are competing with each other to see who can swim 10 laps the fastest. Billy swims his first 5 laps in 2 minutes, swims the next 3 laps in 4 minutes, swims the next lap in 1 minute, then swims his final lap. Margaret finishes swimming all of her laps in 10 minutes. Billy wins the competition by finishing his laps 30 seconds before Margaret does. In seconds, how long did it take Billy to swim his final lap?"""
    # Define the total number of laps
    total_laps = 10

    # Define the time it takes to swim each set of laps
    first_five_time = 2 * 60
    next_three_time = 4 * 60
    next_lap_time = 1 * 60

    # Calculate the time it took Billy to complete the first 9 laps (in seconds)
    first_nine_time = first_five_time + next_three_time + next_lap_time

    # Calculate the time it took Billy to complete all 10 laps (in seconds)
    billy_time = first_nine_time + last_lap_time

    # Calculate the time it took Margaret to complete all 10 laps (in seconds)
    margaret_time = 10 * 60

    # Calculate the time difference between Billy and Margaret (in seconds)
    time_difference = margaret_time - billy_time + 30

    # Calculate the time it took Billy to swim his final lap (in seconds)
    last_lap_time = time_difference / 2

    result = last_lap_time
    return result

print(solution())