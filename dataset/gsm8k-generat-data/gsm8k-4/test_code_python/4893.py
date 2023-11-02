def solution():
    """Camp Cedar has 40 boys, it has 3 times as many girls. It needs 1 counselor for every 8 children. How many counselors does Camp Cedar need?"""
    # Define the number of boys
    boys = 40

    # Calculate the number of girls
    girls = boys * 3

    # Calculate the total number of children
    total_children = boys + girls

    # Calculate the number of counselors needed
    counselors = total_children // 8

    # If there are any remaining children, add an additional counselor
    if total_children % 8 != 0:
        counselors += 1

    result = counselors
    return result

print(solution())