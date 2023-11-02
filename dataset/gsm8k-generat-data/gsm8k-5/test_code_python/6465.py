def solution():
    # Calculate the total rainfall for the first three days
    total_rainfall = 26 + 34 + (34 - 12)  # On the third day, 12 cm less than the second day fell

    # Find the difference between the actual rainfall and the average rainfall
    difference = 140 - total_rainfall

    result = difference
    return result

print(solution())