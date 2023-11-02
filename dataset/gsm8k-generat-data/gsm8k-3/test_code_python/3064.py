def solution():
    """Buying a toaster requires an insurance plan that is 20% of the MSRP, plus a mandatory state tax rate of 50% after the insurance plan calculation.
    Jon chooses to buy a toaster that costs $30 at MSRP. What is the total he must pay?"""
    # Define the MSRP of the toaster
    MSRP = 30

    # Calculate the cost of the insurance plan
    insurance_cost = MSRP * 0.2

    # Calculate the total cost with the insurance plan
    total_cost_insurance = MSRP + insurance_cost

    # Calculate the state tax
    state_tax = total_cost_insurance * 0.5

    # Calculate the total cost with the insurance plan and state tax
    total_cost = total_cost_insurance + state_tax

    # Display the total cost
    result = total_cost
    return result

print(solution())