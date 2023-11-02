def solution():
    """Camp Cedar has 40 boys, it has 3 times as many girls. It needs 1 counselor for every 8 children. How many counselors does Camp Cedar need?"""
    boys = 40
    girls = boys * 3
    children = boys + girls
    counselors_needed = children // 8
    result = counselors_needed
    return result

print(solution())