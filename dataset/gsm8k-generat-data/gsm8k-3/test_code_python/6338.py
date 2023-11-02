def solution():
    """Lisa bought a new iPhone for $1000. She bought a phone contract that costs $200/month, a case that costs 20% of the cost of the phone, and headphones that cost half as much as the case. How much will Lisa spend on her phone in the first year?"""
    # Define the cost of the phone and the monthly phone contract
    PHONE_COST = 1000
    CONTRACT_COST = 200

    # Calculate the cost of the phone case and headphones
    case_cost = PHONE_COST * 0.2
    headphone_cost = case_cost / 2

    # Calculate the total cost of the phone and accessories
    total_cost = PHONE_COST + case_cost + headphone_cost

    # Calculate the total cost of the phone contract for a year
    contract_yearly_cost = CONTRACT_COST * 12

    # Calculate the total cost for the first year
    total_yearly_cost = total_cost + contract_yearly_cost

    # Display the total cost for the first year
    result = total_yearly_cost
    return result

print(solution())