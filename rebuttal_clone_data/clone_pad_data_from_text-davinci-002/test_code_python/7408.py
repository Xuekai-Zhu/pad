def solution():
    initial_rainfall = 5
    second_rainfall = initial_rainfall / 2
    third_rainfall = second_rainfall / 2
    total_rainfall = initial_rainfall + second_rainfall + third_rainfall
    average_rainfall = total_rainfall / 3
    result = average_rainfall
    
    return result

print(solution())