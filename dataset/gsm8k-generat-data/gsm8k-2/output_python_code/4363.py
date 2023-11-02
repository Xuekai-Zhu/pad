def solution():
    """Jackson wants to improve his endurance running. His goal is to start by running 3 miles a day the first week, then spend the next four weeks running one additional mile/day each week. How many miles is Jackson running each day at the end of this exercise program?"""
    starting_week = 3
    first_week = starting_week
    second_week = first_week + 1
    third_week = second_week + 1
    fourth_week = third_week + 1
    total_miles = first_week + second_week + third_week + fourth_week
    average_miles = total_miles / 28
    result = average_miles
    return result

print(solution())