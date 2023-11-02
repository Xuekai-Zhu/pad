def solution():
    """Camp Cedar has 40 boys, it has 3 times as many girls.  It needs 1 counselor for every 8 children.  How many counselors does Camp Cedar need?"""
    # Calculate the number of girls
    girls = 3 * 40

    # Calculate the total number of children
    children = boys + girls

    # Calculate the number of counselors needed
    counselors = children // 8

    # Display the number of counselors needed
    result = counselors
    return result

print(solution())