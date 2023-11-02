def solution():
    total_ride = 1000
    first_sign = 350
    second_sign = total_ride - (first_sign + 275)
    result = second_sign - first_sign
    return result

print(solution())