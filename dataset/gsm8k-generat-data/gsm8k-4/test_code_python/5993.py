def solution():
    """John wants to lose weight. He eats 1800 calories a day and burns 2300 a day. If he needs to burn 4000 calories to lose 1 pound how many days will it take to lose 10 pounds?"""
    # Define the daily caloric intake and burn
    daily_intake = 1800
    daily_burn = 2300

    # Calculate the caloric deficit per day
    caloric_deficit = daily_burn - daily_intake

    # Calculate the caloric deficit needed to lose 10 pounds
    total_deficit = 4000 * 10

    # Calculate the number of days needed to reach the total caloric deficit
    days_needed = total_deficit / caloric_deficit

    result = round(days_needed)
    return result

print(solution())