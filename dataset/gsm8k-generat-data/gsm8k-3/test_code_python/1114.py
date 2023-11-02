def solution():
    """Jeff makes 10 donuts each day for 12 days. Jeff eats one of the donuts each day. Chris then comes over and eats 8 donuts. If 10 donuts fit in each box, how many boxes can Jeff fill with his donuts?"""
    # Calculate the total number of donuts Jeff makes
    total_donuts = 10 * 12

    # Subtract the number of donuts Jeff eats and the number Chris eats
    remaining_donuts = total_donuts - 12 - 8

    # Calculate the number of boxes Jeff can fill
    boxes = remaining_donuts // 10

    # Display the number of boxes Jeff can fill
    result = boxes
    return result

print(solution())