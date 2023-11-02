def solution():
    gift_amount = 50
    tape_cost = 9
    num_tapes = 2
    headphone_cost = 25

    # Calculate the total cost of the two cassette tapes
    total_tape_cost = tape_cost * num_tapes

    # Calculate the total cost of all items Josie plans to buy
    total_cost = total_tape_cost + headphone_cost

    # Calculate the amount of money Josie will have left after buying all items
    money_left = gift_amount - total_cost
    result = money_left
    return result

print(solution())