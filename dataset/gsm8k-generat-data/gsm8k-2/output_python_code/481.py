def solution():
    """Ian is looking to lose some weight. He decides to start jogging around his apartment complex every night to burn some calories. He does 5 laps around the complex every night. Each lap is 100 feet. If it takes 25 feet of jogging to burn a calorie, how many calories does Ian burn after 5 days of jogging like this?"""
    laps_per_night = 5
    lap_distance = 100
    total_distance = laps_per_night * lap_distance
    feet_per_calorie = 25
    total_calories = (total_distance / feet_per_calorie) * 5
    result = total_calories
    return result

print(solution())