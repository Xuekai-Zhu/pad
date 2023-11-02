def solution():
    """Ian is looking to lose some weight. He decides to start jogging around his apartment complex every night to burn some calories. He does 5 laps around the complex every night. Each lap is 100 feet. If it takes 25 feet of jogging to burn a calorie, how many calories does Ian burn after 5 days of jogging like this?"""
    laps_per_day = 5
    lap_distance = 100
    total_distance = laps_per_day * lap_distance
    calories_per_foot = 1 / 25
    calories_burned = total_distance * calories_per_foot
    total_days = 5
    total_calories_burned = calories_burned * total_days
    result = total_calories_burned
    return result

print(solution())