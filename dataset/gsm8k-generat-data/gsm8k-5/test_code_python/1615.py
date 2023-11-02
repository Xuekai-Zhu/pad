def solution():
    soap_per_month = 1  # Elias uses a bar of soap every month
    cost_per_bar = 4  # Each bar of soap costs $4
    months_in_two_years = 24  # There are 24 months in two years

    # Calculate the total cost of soap in two years
    total_cost = soap_per_month * cost_per_bar * months_in_two_years
    result = total_cost
    return result

print(solution())