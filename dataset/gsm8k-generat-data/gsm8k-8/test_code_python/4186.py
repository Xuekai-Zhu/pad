def solution():
    # Calculate the number of loot boxes John bought
    num_boxes = 40 / 5

    # Calculate the total amount of money John spent on items inside the loot boxes
    total_spent = num_boxes * 3.5

    # Calculate the average amount John lost per loot box
    average_loss = 5 - (total_spent / num_boxes)
    result = average_loss
    return result

print(solution())