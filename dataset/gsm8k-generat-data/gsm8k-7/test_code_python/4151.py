def solution():
    can_weight = 2  # ounces
    bottle_weight = 6  # ounces
    max_weight = 100  # ounces
    num_cans = 20
    bottle_price = 10  # cents per bottle
    can_price = 3  # cents per can

    # Calculate the weight of the cans
    total_can_weight = num_cans * can_weight

    # Calculate the remaining weight for bottles
    remaining_weight = max_weight - total_can_weight

    # Calculate the number of bottles that Jenny can carry
    num_bottles = remaining_weight // bottle_weight

    # Calculate the total amount of money that Jenny will make
    total_money = (num_bottles * bottle_price) + (num_cans * can_price)

    result = total_money
    return result

print(solution())