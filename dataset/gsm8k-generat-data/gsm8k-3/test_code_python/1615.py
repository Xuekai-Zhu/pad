def solution():
    """Elias uses a bar of soap every month. If each bar of soap costs $4, how much does he spend on bars of soap in two years?"""
    # Define the cost of one bar of soap
    SOAP_COST = 4

    # Calculate the number of bars of soap Elias uses in 2 years (24 months)
    soap_used = 24

    # Calculate the total cost of soap used in 2 years
    total_cost = soap_used * SOAP_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())