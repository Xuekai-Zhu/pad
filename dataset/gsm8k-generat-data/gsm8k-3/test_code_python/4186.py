def solution():
    """John buys game loot boxes for $5 each. The average value of items inside is $3.5. He spends $40 on loot boxes. What is the average amount he lost?"""
    # Define the cost and average value of each loot box
    BOX_COST = 5
    AVERAGE_VALUE = 3.5

    # Calculate the number of loot boxes purchased
    num_boxes = 40 / BOX_COST

    # Calculate the total value of all the items received
    total_value = num_boxes * AVERAGE_VALUE

    # Calculate the total cost of all the loot boxes
    total_cost = num_boxes * BOX_COST

    # Calculate the average amount lost per loot box
    average_loss = BOX_COST - AVERAGE_VALUE

    # Calculate the total amount lost
    total_loss = num_boxes * average_loss

    # Display the total amount lost
    result = total_loss
    return result

print(solution())