def solution():
    """Jerry is trying to cut down on the amount of soda he drinks. Right now, he drinks 48 sodas a week. If he cuts the number of sodas he drinks in half each week, how many weeks will it take him to only drink 6 sodas per week?"""
    # Define the initial number of sodas Jerry drinks per week
    INITIAL_SODAS = 48

    # Define the final number of sodas Jerry wants to drink per week
    FINAL_SODAS = 6

    # Start with the initial number of sodas and keep dividing by 2 each week until we reach the final number
    sodas = INITIAL_SODAS
    weeks = 0
    while sodas > FINAL_SODAS:
        sodas /= 2
        weeks += 1

    # Display the number of weeks it takes for Jerry to reach his goal
    result = weeks
    return result

print(solution())