def solution():
    """To improve her health, Mary decides to drink 1.5 liters of water a day as recommended by her doctor. Mary's glasses hold 250 mL of water. How many glasses of water should Mary drink per day to reach her goal?"""
    # Define the goal amount of water to drink per day in liters
    GOAL_AMOUNT = 1.5

    # Convert the goal amount to milliliters
    goal_milliliters = GOAL_AMOUNT * 1000

    # Calculate the number of glasses of water Mary should drink per day
    glasses_per_day = goal_milliliters / 250

    # Round up to the nearest whole number of glasses
    glasses_per_day = math.ceil(glasses_per_day)

    # Display the number of glasses of water Mary should drink per day
    result = glasses_per_day
    return result

print(solution())