def solution():
    """Jeremy buys 30 watermelons. He eats 3 watermelons per week. Each week he gives 2 to his dad. How many weeks will the watermelons last?"""
    # Define the initial number of watermelons
    watermelons = 30

    # Define the number of watermelons that Jeremy eats and gives to his dad each week
    weekly_consumption = 3 + 2

    # Calculate the number of weeks that the watermelons will last
    weeks = watermelons // weekly_consumption

    # return the result
    result = weeks
    return result

print(solution())