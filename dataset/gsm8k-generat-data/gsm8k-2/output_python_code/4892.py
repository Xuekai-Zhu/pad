def solution():
    """Camp Cedar has 40 boys, it has 3 times as many girls. It needs 1 counselor for every 8 children. How many counselors does Camp Cedar need?"""
    boys = 40
    girls = 3 * boys
    total_children = boys + girls
    counselors = total_children / 8
    result = counselors
    return result

print(solution())