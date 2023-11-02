def solution():
    """40 kids are running a race. 10% of them pass the finish line in less than 6 minutes. Three times that number finish in less than 8 minutes. 1/6 of the remaining kids take more than 14 minutes. How many kids take more than 14 minutes?"""
    total_kids = 40
    less_than_6 = total_kids * 0.1
    less_than_8 = 3 * less_than_6
    remaining = total_kids - less_than_6 - less_than_8
    more_than_14 = remaining / 6
    result = more_than_14
    return result

print(solution())