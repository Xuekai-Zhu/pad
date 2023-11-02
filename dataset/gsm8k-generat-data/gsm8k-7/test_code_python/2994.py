def solution():
    time_spent_hosing_off = 10
    num_shampoos = 3
    time_per_shampoo = 15

    # Calculate the total time spent shampooing
    total_time_shampooing = num_shampoos * time_per_shampoo

    # Calculate the total time spent cleaning the dog
    total_time_cleaning = time_spent_hosing_off + total_time_shampooing
    result = total_time_cleaning
    return result

print(solution())