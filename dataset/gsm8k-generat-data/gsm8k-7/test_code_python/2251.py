def solution():
    gas_cost = 17
    num_lawns = 3
    lawn_charge = 12
    extra_income = 10

    # Calculate the total income from mowing lawns
    lawn_income = num_lawns * lawn_charge

    # Calculate the total profit by subtracting costs from income
    total_profit = lawn_income + extra_income - gas_cost
    result = total_profit
    return result

print(solution())