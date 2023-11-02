def solution():
    """50% of substitute teachers walk out after 1 hour of teaching. 30% of the remainder quit before lunch. If 60 substitute teachers show up at 7 AM, how many will be left after lunch?"""
    initial_substitutes = 60
    after_one_hour = initial_substitutes / 2
    after_lunch = (after_one_hour * 0.7)
    result = after_lunch
    return result

print(solution())