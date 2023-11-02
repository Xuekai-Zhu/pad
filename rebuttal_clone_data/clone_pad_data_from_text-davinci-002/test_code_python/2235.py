def solution():
    cups_of_rice_morning = 3
    cups_of_rice_afternoon = 2
    cups_of_rice_evening = 5
    grams_of_fat_per_cup = 10
    total_grams_of_fat = (cups_of_rice_morning + cups_of_rice_afternoon + cups_of_rice_evening) * grams_of_fat_per_cup
    result = total_grams_of_fat
    return result

print(solution())