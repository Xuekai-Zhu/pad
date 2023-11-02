def solution():
    customers_per_month = 80  # Vince serves 80 customers per month
    earnings = customers_per_month * 18  # Vince earns $18 per customer
    expenses = 280 + (earnings * 0.2)  # Vince spends 20% of his earnings on recreation and relaxation

    # Calculate Vince's savings
    savings = earnings - expenses
    result = savings
    return result

print(solution())