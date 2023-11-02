def solution():
    """John buys game loot boxes for $5 each. The average value of items inside is $3.5. He spends $40 on loot boxes. What is the average amount he lost?"""
    loot_box_cost = 5
    average_value = 3.5
    num_boxes = 40 / loot_box_cost
    total_value = num_boxes * average_value
    average_loss = loot_box_cost - (total_value / num_boxes)
    result = average_loss
    return result

print(solution())