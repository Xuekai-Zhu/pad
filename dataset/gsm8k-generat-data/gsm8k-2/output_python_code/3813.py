def solution():
    """Andre catches 8 ladybugs on Monday and 5 ladybugs on Tuesday. If each ladybug has 6 dots, how many dots are there in total for all the ladybugs?"""
    monday_ladybugs = 8
    tuesday_ladybugs = 5
    dots_per_ladybug = 6
    total_ladybugs = monday_ladybugs + tuesday_ladybugs
    total_dots = total_ladybugs * dots_per_ladybug
    result = total_dots
    return result

print(solution())