def solution():
    """The difference between the number of boys and girls in a tree planting event is 400. If there are 600 boys at the event, and the number of girls is more than the number of boys, what's 60% of the total number of boys and girls at the event?"""
    boys = 600
    girls = boys + 400
    total_people = boys + girls
    total_percentage = 0.6 * total_people
    result = total_percentage
    return result

print(solution())