def solution():
    """The difference between the number of boys and girls in a tree planting event is 400. If there are 600 boys at the event, and the number of girls is more than the number of boys, what's 60% of the total number of boys and girls at the event?"""
    # Define the number of boys and the difference
    boys = 600
    difference = 400

    # Calculate the number of girls
    girls = boys + difference

    # Calculate the total number of participants
    total = boys + girls

    # Calculate 60% of the total number of participants
    percentage = 0.6
    result = total * percentage
    return result

print(solution())