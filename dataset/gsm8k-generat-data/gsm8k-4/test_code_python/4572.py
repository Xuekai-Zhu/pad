def solution():
    """Jon drinks a bottle of water that is 16 ounces every 4 hours for the 16 hours he is awake. Twice a day he also drinks a bottle that is 25% larger than those bottles. How much fluid does he drink a week?"""
    # Define the volume of the regular water bottle and the frequency of consumption
    regular_bottle = 16  # ounces
    regular_frequency = 4  # hours

    # Define the volume of the larger water bottle and the frequency of consumption
    larger_bottle = regular_bottle * 1.25  # ounces
    larger_frequency = 12  # hours (twice a day)

    # Calculate the daily fluid intake from regular bottles
    regular_intake = regular_bottle * (16 / regular_frequency)  # ounces/hour * hours = ounces

    # Calculate the daily fluid intake from larger bottles
    larger_intake = larger_bottle * (2 / larger_frequency)  # ounces/hour * hours = ounces

    # Calculate the total daily fluid intake
    total_intake = regular_intake + larger_intake  # ounces

    # Calculate the weekly fluid intake
    weekly_intake = total_intake * 7  # ounces/week

    result = weekly_intake
    return result

print(solution())