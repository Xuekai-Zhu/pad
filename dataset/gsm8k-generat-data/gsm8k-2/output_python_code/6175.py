def solution():
    """There are 34 kids signed up to compete in the talent show. There are 22 more girls than boys signed up to compete. How many girls are signed up to compete in the talent show?"""
    total_kids = 34
    boys = (total_kids - 22) / 2
    girls = boys + 22
    result = girls
    return result

print(solution())