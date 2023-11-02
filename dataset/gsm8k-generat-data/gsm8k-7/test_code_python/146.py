def solution():
    time_to_clean_richard = 22
    time_to_clean_cory = time_to_clean_richard + 3
    time_to_clean_blake = time_to_clean_cory - 4
    num_cleaning_sessions = 2

    # Calculate the total time Richard spends cleaning his room each week
    richard_time = time_to_clean_richard * num_cleaning_sessions

    # Calculate the total time Cory spends cleaning her room each week
    cory_time = time_to_clean_cory * num_cleaning_sessions

    # Calculate the total time Blake spends cleaning his room each week
    blake_time = time_to_clean_blake * num_cleaning_sessions

    # Calculate the total time all three spend cleaning their rooms each week
    total_time = richard_time + cory_time + blake_time
    result = total_time
    return result

print(solution())