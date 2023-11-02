def solution():
    first_test = 95
    second_test = 80
    desired_average = 90
    total_average = (first_test + second_test) / 2
    third_test = (desired_average * 3) - (first_test + second_test)
    result = third_test
    return result

print(solution())