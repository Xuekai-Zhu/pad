def solution():
    """The difference between the number of boys and girls in a tree planting event is 400. If there are 600 boys at the event, and the number of girls is more than the number of boys, what's 60% of the total number of boys and girls at the event?"""
    boys = 600
    girls = boys + 400
    total = boys + girls
    percentage = 60
    result = (percentage/100) * total
    return result

print(solution())