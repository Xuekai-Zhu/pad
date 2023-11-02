def solution():
    
    calories_per_hour_aerobics = 500
    hours_aerobics = 2
    calories_burned_aerobics = 500
    hours_running = 1
    calories_burned_running = 600
    ml_per_200_calories = 100
    total_calories_aerobics = hours_aerobics * calories_burned_aerobics
    total_calories_running = hours_running * calories_burned_running
    total_calories_drunk = total_calories_aerobics + total_calories_running
    ml_needed = total_calories_drunk / 200_calories
    result = ml_needed
    return result

print(solution())