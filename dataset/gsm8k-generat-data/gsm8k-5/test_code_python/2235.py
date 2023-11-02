def solution():
    rice_per_week = (3 + 2 + 5) * 7  # Robbie eats 3 cups in the morning, 2 cups in the afternoon, and 5 cups in the evening, for 7 days
    fat_per_cup = 10  # Each cup of rice has 10 grams of fat

    # Calculate the total fat intake per week
    total_fat = rice_per_week * fat_per_cup
    result = total_fat
    return result

print(solution())