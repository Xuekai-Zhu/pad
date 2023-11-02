def solution():
    money_found = 12  # David found $12
    money_owned = 1  # Evan has $1
    item_cost = 20  # Evan needs to buy a watch worth $20

    # Calculate how much money Evan needs to buy the watch
    money_needed = item_cost - (money_found + money_owned)

    result = money_needed
    return result

print(solution())