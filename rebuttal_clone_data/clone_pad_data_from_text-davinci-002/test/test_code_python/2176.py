def solution():
    calories_in_one_slice = 350
    total_calories = 2800
    percent_eaten = 25
    calories_eaten = total_calories * (percent_eaten / 100)
    slices_eaten = calories_eaten / calories_in_one_slice
    result = slices_eaten
    return result

print(solution())