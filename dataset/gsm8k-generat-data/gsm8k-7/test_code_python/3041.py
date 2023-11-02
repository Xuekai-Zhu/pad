def solution():
    miles_first_day = 125
    miles_second_day = 223
    total_miles = 493

    # Calculate the miles driven on the third day
    miles_third_day = total_miles - miles_first_day - miles_second_day
    result = miles_third_day
    return result

print(solution())