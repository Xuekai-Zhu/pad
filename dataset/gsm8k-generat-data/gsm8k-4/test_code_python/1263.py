def solution():
    """Phil has a coin collection he likes to add to. He started with 50 state quarters his parents gave him. Over the next year he doubled this. The following year he collected 3 each month. The year after that he collected 1 every third month. The year after that he lost a quarter of them when he misplaced his collection. How many did he have left after losing some?"""
    # Define the starting number of state quarters
    state_quarters = 50

    # Double the number of state quarters from the previous year
    state_quarters *= 2

    # Add 3 quarters each month for a year
    state_quarters += 3 * 12

    # Add 1 quarter every third month for a year
    state_quarters += 1 * 4

    # Calculate the number of quarters lost
    lost_quarters = int(state_quarters * 0.25)

    # Calculate the remaining number of quarters
    remaining_quarters = state_quarters - lost_quarters

    # return the result
    result = remaining_quarters
    return result

print(solution())