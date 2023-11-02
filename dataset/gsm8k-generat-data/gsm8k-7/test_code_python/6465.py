def solution():
    first_day_rainfall = 26
    second_day_rainfall = 34
    third_day_rainfall = second_day_rainfall - 12
    average_rainfall = 140

    # Calculate the total rainfall in the first three days of May
    total_rainfall = first_day_rainfall + second_day_rainfall + third_day_rainfall

    # Calculate the difference between the total rainfall and the average rainfall
    difference = average_rainfall - total_rainfall
    result = difference
    return result

print(solution())