def solution():
    """Jamie's father gained 5 pounds over the holidays that he wants to lose so his pants will not be as snug. He asks Jamie to help him keep track of his calories. Jamie's father burns 2,500 calories of fat a day by doing light exercise. There are 3,500 calories in a pound of body fat. How many days will it take for Jamie's father to burn off 5 pounds if he does light exercise and sticks to eating 2000 calories a day?"""
    # Define the number of calories burned per day and the number of calories in a pound of body fat
    CALORIES_BURNED_PER_DAY = 2500
    CALORIES_PER_POUND_OF_FAT = 3500

    # Define the target weight loss in pounds and the daily calorie deficit
    WEIGHT_LOSS = 5
    DAILY_CALORIE_DEFICIT = 500

    # Calculate the total calorie deficit required to lose the target weight
    total_calorie_deficit = WEIGHT_LOSS * CALORIES_PER_POUND_OF_FAT

    # Calculate the number of days required to achieve the target weight loss
    days_required = total_calorie_deficit / (CALORIES_BURNED_PER_DAY - DAILY_CALORIE_DEFICIT)

    # Return the result
    result = round(days_required)
    return result

print(solution())