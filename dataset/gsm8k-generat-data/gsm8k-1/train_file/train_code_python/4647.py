def solution():
    """Vince owns a hair salon and he earns $18 per head. His monthly expenses are $280 for rent and electricity and 20% of his earnings are allocated for recreation and relaxation. He will save the rest. How much does he save if he serves 80 customers a month?"""
    price_per_head = 18
    num_customers = 80
    total_earnings = price_per_head * num_customers
    expenses = 280
    recreation_amount = 0.2 * total_earnings
    savings = total_earnings - (expenses + recreation_amount)
    result = savings
    return result

print(solution())