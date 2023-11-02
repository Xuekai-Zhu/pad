def solution():
    """Jackson wants to improve his endurance running. His goal is to start by running 3 miles a day the first week, then spend the next four weeks running one additional mile/day each week. How many miles is Jackson running each day at the end of this exercise program?"""
    starting_miles = 3
    additional_miles = 4
    total_weeks = 5
    end_miles = starting_miles + (additional_miles * (total_weeks - 1))
    miles_per_day = end_miles / 7
    result = miles_per_day
    return result

print(solution())