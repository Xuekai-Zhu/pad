def solution():
    money_given = 50
    pizza_boxes = 2
    pizza_price = 12
    juice_packs = 2
    juice_price = 2

    # Calculate the total cost of all the items
    total_cost = (pizza_boxes * pizza_price) + (juice_packs * juice_price)

    # Calculate the amount of money that Victoria should return
    money_returned = money_given - total_cost
    result = money_returned
    return result

print(solution())