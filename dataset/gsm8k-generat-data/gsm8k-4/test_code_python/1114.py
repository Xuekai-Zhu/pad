def solution():
    """Jeff makes 10 donuts each day for 12 days. Jeff eats one of the donuts each day. Chris then comes over and eats 8 donuts. If 10 donuts fit in each box, how many boxes can Jeff fill with his donuts?"""
    # Define the number of days Jeff makes donuts
    days = 12

    # Calculate the total number of donuts Jeff makes
    total_donuts = days * 10

    # Subtract the donuts Jeff eats and Chris eats
    remaining_donuts = total_donuts - days - 8

    # Calculate the number of boxes Jeff can fill
    boxes = remaining_donuts // 10

    # return the result
    result = boxes
    return result

print(solution())