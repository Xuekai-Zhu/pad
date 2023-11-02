def solution():
    # Number of new coronavirus cases in the first week
    first_week_cases = 5000

    # Number of new coronavirus cases in the second week
    second_week_cases = first_week_cases / 2

    # Number of new coronavirus cases in the third week
    third_week_cases = second_week_cases + 2000

    # Total number of new coronavirus cases in the three weeks
    total_cases = first_week_cases + second_week_cases + third_week_cases
    result = total_cases
    return result

print(solution())