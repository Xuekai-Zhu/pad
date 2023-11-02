def solution():
    total_spent = 610
    num_of_items = 7
    price_of_item_A = 49
    price_of_item_B = 81

    # Calculate the total cost of all items except item A and item B
    total_cost_without_AB = total_spent - price_of_item_A - price_of_item_B

    # Calculate the price of one of the other items
    price_of_other_item = total_cost_without_AB / (num_of_items - 2)

    result = price_of_other_item
    return result

print(solution())