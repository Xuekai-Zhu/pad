def solution():
    """Ian is looking to lose some weight.  He decides to start jogging around his apartment complex every night to burn some calories.  He does 5 laps around the complex every night.  Each lap is 100 feet.  If it takes 25 feet of jogging to burn a calorie, how many calories does Ian burn after 5 days of jogging like this?"""
    
    # Calculate the total distance Ian jogs each night
    lap_distance = 100 * 5
    total_distance = lap_distance * 5

    # Calculate the number of calories burned for the total distance
    calories_burned = total_distance // 25

    # Display the number of calories burned
    result = calories_burned
    return result

print(solution())