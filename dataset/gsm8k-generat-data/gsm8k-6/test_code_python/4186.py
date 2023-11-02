def solution():
    # Calculate the number of loot boxes bought by John
    num_boxes = 40 / 5  # John spent $40 and each loot box cost $5

    # Calculate the average amount lost per loot box
    avg_lost = 5 - 3.5  # the difference between the cost and average value of each loot box

    # Calculate the total amount lost by John
    total_lost = avg_lost * num_boxes

    result = total_lost
    return result

print(solution())