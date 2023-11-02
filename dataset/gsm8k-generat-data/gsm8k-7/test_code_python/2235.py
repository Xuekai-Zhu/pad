def solution():
    rice_morning = 3 # cups of rice in the morning
    rice_afternoon = 2 # cups of rice in the afternoon
    rice_evening = 5 # cups of rice in the evening
    fat_per_cup = 10 # grams of fat per cup of rice
    days_per_week = 7

    # Calculate the total cups of rice Robbie eats per week
    total_rice_weekly = (rice_morning + rice_afternoon + rice_evening) * days_per_week

    # Calculate the total grams of fat Robbie consumes per week
    total_fat_weekly = total_rice_weekly * fat_per_cup
    result = total_fat_weekly
    return result

print(solution())