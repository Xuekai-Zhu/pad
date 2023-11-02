def solution():
    num_lollipops = 4
    lollipop_price = 2

    num_chocolate_packs = 6
    chocolate_price = 4 * lollipop_price

    total_cost = (num_lollipops * lollipop_price) + (num_chocolate_packs * chocolate_price)
    amount_given = 6 * 10

    change = amount_given - total_cost
    result = change
    return result

print(solution())