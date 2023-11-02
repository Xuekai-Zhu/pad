def solution():
    """Ian is looking to lose some weight. He decides to start jogging around his apartment complex every night to burn some calories. He does 5 laps around the complex every night. Each lap is 100 feet. If it takes 25 feet of jogging to burn a calorie, how many calories does Ian burn after 5 days of jogging like this?"""
    # Define the number of laps Ian takes per night
    laps_per_night = 5

    # Define the length of each lap in feet
    lap_length = 100

    # Calculate the total distance Ian jogs in 5 days
    total_distance = laps_per_night * lap_length * 5

    # Calculate the number of calories Ian burns
    calories_burned = total_distance // 25

    # return the result
    result = calories_burned
    return result

print(solution())