def solution():
    total_cost = 260  # The total cost of the heels is $260
    extra_money = 50  # Miranda's sister gave her $50 to add to her savings
    total_savings = total_cost - extra_money  # Miranda's total savings

    # Calculate the savings per month
    savings_per_month = total_savings / 3
    result = savings_per_month
    return result

print(solution())