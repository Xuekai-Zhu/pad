def solution():
    """Buying a toaster requires an insurance plan that is 20% of the MSRP, plus a mandatory state tax rate of 50% after the insurance plan calculation. Jon chooses to buy a toaster that costs $30 at MSRP. What is the total he must pay?"""
    # Define the MSRP of the toaster
    msrp = 30

    # Calculate the cost of the insurance plan
    insurance_cost = msrp * 0.2

    # Calculate the subtotal
    subtotal = msrp + insurance_cost

    # Calculate the state tax
    tax_rate = 0.5
    tax = subtotal * tax_rate

    # Calculate the total cost
    total_cost = subtotal + tax

    # Return the result
    result = total_cost
    return result

print(solution())