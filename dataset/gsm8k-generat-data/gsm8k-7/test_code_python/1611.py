def solution():
    first_day = 200
    second_day = 0.75 * first_day
    third_day = 0.5 * (first_day + second_day)

    total_miles_traveled = first_day + second_day + third_day
    result = total_miles_traveled
    return result

print(solution())