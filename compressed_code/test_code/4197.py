def solution():
    
    first_fastest_age = 10
    second_fastest_age = first_fastest_age - 2
    third_fastest_age = second_fastest_age + 4
    fourth_fastest_age = third_fastest_age / 2
    fifth_fastest_age = fourth_fastest_age + 20
    average_age = (first_fastest_age + fifth_fastest_age) / 2
    result = average_age
    return result

print(solution())