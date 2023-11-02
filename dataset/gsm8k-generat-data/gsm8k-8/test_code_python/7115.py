def solution():
    # Calculate the percentage of mornings that Jake trips over his dog
    trip_percentage = 40

    # Calculate the percentage of times that Jake drops his coffee when he trips
    drop_percentage = 25

    # Calculate the percentage of mornings that Jake does not drop his coffee (by subtracting the percentage of times he drops his coffee from the total percentage of times he trips)
    no_drop_percentage = (100 - drop_percentage) * (100 - trip_percentage) / 100

    result = no_drop_percentage
    return result

print(solution())