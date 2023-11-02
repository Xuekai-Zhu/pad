def solution():
    # Define the number of laps and distance per lap
    num_laps = 5
    lap_distance = 100

    # Calculate the total distance jogged
    total_distance = num_laps * lap_distance

    # Calculate the number of calories burned
    calories_per_foot = 1 / 25
    calories_burned = total_distance * calories_per_foot

    # Calculate the calories burned after 5 days
    days = 5
    calories_burned_total = days * calories_burned
    result = calories_burned_total
    return result

print(solution())