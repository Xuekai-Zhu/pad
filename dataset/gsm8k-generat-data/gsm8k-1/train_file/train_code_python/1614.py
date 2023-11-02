def solution():
    """Elias uses a bar of soap every month. If each bar of soap costs $4, how much does he spend on bars of soap in two years?"""
    soap_per_month = 1
    months_in_two_years = 24
    cost_per_bar = 4
    total_cost = soap_per_month * months_in_two_years * cost_per_bar
    result = total_cost
    return result

print(solution())