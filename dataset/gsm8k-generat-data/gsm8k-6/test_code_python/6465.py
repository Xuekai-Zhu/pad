def solution():
    # Calculate the total rainfall for the first three days
    total_rainfall = 26 + 34 + (34-12)  # on the third day, 12 cm less than the second day fell

    # Calculate the difference between the actual rainfall and the average rainfall for the first three days
    difference = 140 - total_rainfall
    result = difference
    return result

print(solution())