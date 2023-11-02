def solution():
    loot_box_cost = 5.0
    average_item_value = 3.5
    total_spent = 40.0

    # Calculate the number of loot boxes John bought
    num_boxes = total_spent / loot_box_cost

    # Calculate the total value of the items in the loot boxes
    total_value = num_boxes * average_item_value

    # Calculate the average amount John lost per loot box
    average_loss = loot_box_cost - (total_value / num_boxes)
    result = average_loss
    return result

print(solution())