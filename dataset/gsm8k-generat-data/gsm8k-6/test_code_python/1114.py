def solution():
    # Calculate the total number of donuts Jeff makes
    total_donuts = 10*12  # Jeff makes 10 donuts each day for 12 days

    # Subtract the donuts Jeff eats and the donuts Chris eats from the total donuts
    remaining_donuts = total_donuts - 12 - 8  # Jeff eats 1 donut each day for 12 days, Chris eats 8 donuts

    # Calculate the number of boxes Jeff can fill with his remaining donuts
    boxes_filled = remaining_donuts // 10  # 10 donuts fit in each box

    result = boxes_filled
    return result

print(solution())