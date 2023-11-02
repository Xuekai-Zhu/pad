def solution():
    
    cheezit_size = 2 
    cheezit_calories = 150 
    num_bags = 3
    total_cheezit_calories = cheezit_size * cheezit_calories * num_bags
    run_time = 40 
    calories_burnt_per_minute = 12
    total_calories_burnt = run_time * calories_burnt_per_minute
    excess_calories = total_cheezit_calories - total_calories_burnt
    result = excess_calories
    return result

print(solution())