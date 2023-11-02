def solution():
    """Lisa has 36 candies. On Mondays and Wednesdays, she eats 2 candies for each day and on the other days of the week she eats 1 candy for each day. How many weeks does it take for Lisa to eat all of the candies?"""
    # Define the total number of candies
    total_candies = 36

    # Define the number of candies eaten on Mondays and Wednesdays
    candy_per_day_MW = 2
    MW_days = 2

    # Define the number of candies eaten on other days
    candy_per_day_other = 1
    other_days = 5 - MW_days

    # Initialize the number of weeks counter
    weeks = 0

    while total_candies > 0:
        # Increment the week counter
        weeks += 1

        # Calculate the number of candies eaten in this week
        candies_this_week = MW_days * candy_per_day_MW + other_days * candy_per_day_other

        # Subtract the candies eaten from the total number of candies
        total_candies -= candies_this_week

    # Return the number of weeks it took Lisa to eat all of the candies
    result = weeks
    return result

print(solution())