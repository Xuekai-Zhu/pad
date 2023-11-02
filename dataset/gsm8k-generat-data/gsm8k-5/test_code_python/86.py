def solution():
    starting_money = 2  # Peter brings $2
    final_money = 2.5  # Peter leaves with $0.50
    money_spent = starting_money - final_money  # Calculate how much money Peter spent
    cost_per_ounce = 0.25  # The soda costs $0.25 per ounce

    # Calculate how many ounces of soda Peter bought
    ounces_of_soda = money_spent / cost_per_ounce
    result = ounces_of_soda
    return result

print(solution())