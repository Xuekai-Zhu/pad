def solution():
    # Calculate how much Roger paid as down payment
    down_payment = 0.2 * 100000  # 20% of $100,000

    # Calculate the remaining balance after down payment
    remaining_balance = 100000 - down_payment

    # Calculate how much Roger's parents paid off
    parents_payment = 0.3 * remaining_balance  # 30% of remaining balance

    # Calculate the final balance
    final_balance = remaining_balance - parents_payment

    result = final_balance
    return result

print(solution())