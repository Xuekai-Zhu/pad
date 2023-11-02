def solution():
    
    
    first_day_rainfall = 26
    second_day_rainfall = 34
    third_day_rainfall = second_day_rainfall - 12
    total_rainfall = first_day_rainfall + second_day_rainfall + third_day_rainfall

    
    average_rainfall = 140
    difference = average_rainfall - total_rainfall

    return difference

print(solution())