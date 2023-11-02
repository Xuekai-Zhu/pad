def solution():
    num_trains = 4
    num_carriages_per_train = 4
    num_wheels_per_row = 5
    num_rows_per_carriage = 3

    # Calculate the total number of wheels per carriage
    total_wheels_per_carriage = num_rows_per_carriage * num_wheels_per_row

    # Calculate the total number of carriages
    total_carriages = num_trains * num_carriages_per_train

    # Calculate the total number of wheels
    total_wheels = total_carriages * total_wheels_per_carriage
    result = total_wheels
    return result

print(solution())