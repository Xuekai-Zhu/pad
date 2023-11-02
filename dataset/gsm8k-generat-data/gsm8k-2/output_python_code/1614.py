def solution():
    """Elias uses a bar of soap every month. If each bar of soap costs $4, how much does he spend on bars of soap in two years?"""
    soap_per_month = 1
    soap_cost = 4
    num_of_months = 24
    total_spent = soap_per_month * soap_cost * num_of_months
    result = total_spent
    return result

print(solution())