def solution():
    """There are 34 kids signed up to compete in the talent show. There are 22 more girls than boys signed up to compete. How many girls are signed up to compete in the talent show?"""
    total_kids = 34
    # Let's assume x = the number of boys
    x = (total_kids - 22) / 2
    # The number of girls is 22 more than the number of boys
    num_girls = x + 22
    result = num_girls
    return result

print(solution())