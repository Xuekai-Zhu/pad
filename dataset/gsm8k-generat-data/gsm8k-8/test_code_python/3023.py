def solution():
    # Calculate the total amount of money Lola and Dora have
    total_money = 9 + 9

    # Calculate the amount of money left after buying the deck of playing cards
    left_money = total_money - 10

    # Calculate the cost of one box of stickers
    box_cost = 2

    # Calculate the number of boxes they bought
    num_boxes = left_money // box_cost

    # Split the boxes evenly between Lola and Dora
    dora_boxes = num_boxes // 2

    result = dora_boxes
    return result

print(solution())