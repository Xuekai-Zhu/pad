def solution():
    """There are 34 kids signed up to compete in the talent show. There are 22 more girls than boys signed up to compete. How many girls are signed up to compete in the talent show?"""
    # Let x be the number of boys signed up
    x = (34 - 22) / 2
    # Let y be the number of girls signed up
    y = x + 22

    # Display the number of girls signed up
    result = y
    return result

print(solution())