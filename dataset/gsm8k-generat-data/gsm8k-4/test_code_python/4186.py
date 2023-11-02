def solution():
    """John buys game loot boxes for $5 each. The average value of items inside is $3.5. He spends $40 on loot boxes. What is the average amount he lost?"""
    # Define the cost and value of each loot box
    LOOT_BOX_COST = 5
    LOOT_BOX_VALUE = 3.5

    # Define the total amount spent on loot boxes
    total_spent = 40

    # Calculate the number of loot boxes purchased
    num_loot_boxes = total_spent / LOOT_BOX_COST

    # Calculate the total value of items inside the loot boxes
    total_value = num_loot_boxes * LOOT_BOX_VALUE

    # Calculate the average amount lost per loot box
    average_loss = LOOT_BOX_COST - LOOT_BOX_VALUE

    # Calculate the average amount lost per purchase
    average_loss_per_purchase = (total_spent - total_value) / num_loot_boxes

    # Return the result
    result = round(average_loss_per_purchase, 2)
    return result

print(solution())