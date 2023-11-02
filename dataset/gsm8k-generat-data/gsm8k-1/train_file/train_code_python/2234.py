def solution():
    """Robbie is tracking his nutrition intake per week. He eats 3 cups of rice in the morning, 2 cups of rice in the afternoon, and 5 cups of rice in the evening. If a cup of rice has 10 grams of fat, how many grams of fat does Robbie get in a week?"""
    morning_rice = 3
    afternoon_rice = 2
    evening_rice = 5
    cups_per_week = (morning_rice + afternoon_rice + evening_rice) * 7
    fat_per_cup = 10
    fat_per_week = cups_per_week * fat_per_cup
    result = fat_per_week
    return result

print(solution())