def solution():
    """Robbie is tracking his nutrition intake per week. He eats 3 cups of rice in the morning, 2 cups of rice in the afternoon, and 5 cups of rice in the evening. If a cup of rice has 10 grams of fat, how many grams of fat does Robbie get in a week?"""
    # Define the amount of rice eaten in each meal
    morning_rice = 3 # cups
    afternoon_rice = 2 # cups
    evening_rice = 5 # cups

    # Define the amount of fat per cup of rice
    fat_per_cup = 10 # grams

    # Calculate the total amount of rice eaten in a week
    total_rice = (morning_rice + afternoon_rice + evening_rice) * 7 # cups

    # Calculate the total amount of fat consumed in a week
    total_fat = total_rice * fat_per_cup # grams

    # Display the total amount of fat consumed
    result = total_fat
    return result

print(solution())