def solution():
    """Robbie is tracking his nutrition intake per week. He eats 3 cups of rice in the morning, 2 cups of rice in the afternoon, and 5 cups of rice in the evening. If a cup of rice has 10 grams of fat, how many grams of fat does Robbie get in a week?"""
    rice_per_week = (3 + 2 + 5) * 7
    fat_grams_per_cup = 10
    total_fat_grams = rice_per_week * fat_grams_per_cup
    result = total_fat_grams
    return result

print(solution())