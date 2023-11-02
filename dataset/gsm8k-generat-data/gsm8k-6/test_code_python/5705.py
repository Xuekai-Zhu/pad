def solution():
    total_money = 90  # Kiki currently has $90
    price_scarf = 2  # scarves are sold at $2 each
    money_spent_on_hats = 0.6 * total_money  # Kiki spends 60% of her money on hats
    money_spent_on_scarves = 0.4 * total_money  # Kiki spends 40% of her money on scarves
    hats_bought = 2 * scarves_bought  # Kiki buys twice as many hats as scarves

    # Solve for the number of scarves Kiki buys
    total_spent = money_spent_on_hats + money_spent_on_scarves
    scarves_bought = (total_money - money_spent_on_hats) / price_scarf
    result = scarves_bought
    return result

print(solution())