def solution():
    """John buys game loot boxes for $5 each. The average value of items inside is $3.5. He spends $40 on loot boxes. What is the average amount he lost?"""
    num_boxes = 40/5 # number of loot boxes purchased
    expected_value = 3.5 # average value of items in the loot boxes
    spent_value = num_boxes*5 # total amount spent on loot boxes
    actual_value = num_boxes*expected_value # total value of items in the loot boxes
    average_loss = (spent_value-actual_value)/num_boxes # average loss per loot box
    result = round(average_loss, 2)
    return result

print(solution())