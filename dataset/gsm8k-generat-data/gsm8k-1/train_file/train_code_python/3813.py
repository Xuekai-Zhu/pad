def solution():
    """Andre catches 8 ladybugs on Monday and 5 ladybugs on Tuesday. If each ladybug has 6 dots, how many dots are there in total for all the ladybugs?"""
    ladybugs_monday = 8
    ladybugs_tuesday = 5
    dots_per_ladybug = 6
    total_dots = (ladybugs_monday + ladybugs_tuesday) * dots_per_ladybug
    result = total_dots
    return result

print(solution())