def solution():
    """Jeremy buys 30 watermelons. He eats 3 watermelons per week. Each week he gives 2 to his dad. How many weeks will the watermelons last?"""
    # Define the initial number of watermelons
    watermelons = 30

    # Define the number of watermelons Jeremy eats per week and gives to his dad
    per_week = 3 + 2

    # Calculate the number of weeks the watermelons will last
    weeks = watermelons // per_week

    # Display the number of weeks
    result = weeks
    return result

print(solution())