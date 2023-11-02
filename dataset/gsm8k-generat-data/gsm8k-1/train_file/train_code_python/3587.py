def solution():
    """A group of bedbugs infested an old mattress. Every day, the number of bedbugs would triple. After four days, there were 810 bedbugs burrowing into the mattress. How many bedbugs did the group start with?"""
    days = 4
    final_count = 810
    starting_count = final_count / (3 ** days)
    result = starting_count
    return result

print(solution())