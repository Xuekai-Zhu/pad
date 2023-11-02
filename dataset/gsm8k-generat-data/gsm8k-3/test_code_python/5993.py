def solution():
    """John wants to lose weight. He eats 1800 calories a day and burns 2300 a day. If he needs to burn 4000 calories to lose 1 pound how many days will it take to lose 10 pounds?"""
    # Define the amount of calories John eats and burns per day
    CALORIES_EATEN = 1800
    CALORIES_BURNED = 2300

    # Define the number of calories John needs to burn to lose 1 pound
    CALORIES_PER_POUND = 4000

    # Define the number of pounds John wants to lose
    pounds_to_lose = 10

    # Calculate the number of calories John needs to burn to achieve his weight loss goal
    total_calories_to_burn = pounds_to_lose * CALORIES_PER_POUND

    # Calculate the number of days it will take for John to achieve his weight loss goal
    days_to_lose_weight = int(total_calories_to_burn / (CALORIES_BURNED - CALORIES_EATEN))

    # Display the number of days it will take for John to achieve his weight loss goal
    result = days_to_lose_weight
    return result

print(solution())