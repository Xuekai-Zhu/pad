def solution():
    cost_per_box = 5  # John buys loot boxes for $5 each
    average_value_per_box = 3.5  # The average value of items in each box is $3.5
    total_spent = 40  # John spends $40 on loot boxes
    num_boxes = total_spent / cost_per_box  # Calculate the number of boxes John buys
    total_value = num_boxes * average_value_per_box  # Calculate the total value of items in the boxes
    total_lost = total_spent - total_value  # Calculate the total amount John lost

    # Calculate the average amount John lost per box
    average_lost_per_box = total_lost / num_boxes
    result = average_lost_per_box
    return result

print(solution())