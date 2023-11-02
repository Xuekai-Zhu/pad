def solution():
    time_for_vacuuming = 45
    time_for_dusting = 60
    time_for_mopping = 30
    time_per_cat = 5
    num_cats = 3
    total_free_time = 3*60 # 3 hours in minutes

    # Calculate the total time it will take Gunther to clean the apartment
    total_time_for_cleaning = time_for_vacuuming + time_for_dusting + (time_for_mopping * 2) + (time_per_cat * num_cats)

    # Calculate the amount of free time Gunther will have left after cleaning the apartment
    free_time_left = total_free_time - total_time_for_cleaning
    result = free_time_left
    return result

print(solution())