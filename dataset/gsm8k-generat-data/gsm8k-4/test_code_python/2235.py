def solution():
    """Robbie is tracking his nutrition intake per week. He eats 3 cups of rice in the morning, 2 cups of rice in the afternoon, and 5 cups of rice in the evening. If a cup of rice has 10 grams of fat, how many grams of fat does Robbie get in a week?"""
    # Define the number of cups of rice eaten each day
    morning_rice = 3
    afternoon_rice = 2
    evening_rice = 5

    # Calculate the total number of cups of rice eaten in a week
    total_rice = (morning_rice + afternoon_rice + evening_rice) * 7

    # Calculate the total number of grams of fat consumed in a week
    fat_grams = total_rice * 10

    # return the result
    result = fat_grams
    return result

print(solution())