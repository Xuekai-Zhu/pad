def solution():
    trains = 4  # There are 4 trains at the station
    carriages_per_train = 4  # Each train has 4 carriages
    rows_per_carriage = 3  # Each carriage has 3 rows of wheels
    wheels_per_row = 5  # Each row has 5 wheels

    # Calculate the total number of wheels at the train station
    total_wheels = trains * carriages_per_train * rows_per_carriage * wheels_per_row
    result = total_wheels
    return result

print(solution())