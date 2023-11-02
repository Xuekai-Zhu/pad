def solution():
    """Jamie's father gained 5 pounds over the holidays that he wants to lose so his pants will not be as snug. He asks Jamie to help him keep track of his calories. Jamie's father burns 2,500 calories of fat a day by doing light exercise. There are 3,500 calories in a pound of body fat. How many days will it take for Jamie's father to burn off 5 pounds if he does light exercise and sticks to eating 2000 calories a day?"""
    # Define the number of calories in a pound of body fat and the daily calorie deficit
    CALORIES_PER_POUND = 3500
    DAILY_CALORIE_DEFICIT = 500

    # Calculate the total calorie deficit needed to lose 5 pounds
    total_calorie_deficit = 5 * CALORIES_PER_POUND

    # Calculate the number of days it will take to burn off the 5 pounds
    days_to_burn_off = total_calorie_deficit / (DAILY_CALORIE_DEFICIT + 2500 - 2000)

    # Display the number of days it will take to burn off the 5 pounds
    result = days_to_burn_off
    return result

print(solution())