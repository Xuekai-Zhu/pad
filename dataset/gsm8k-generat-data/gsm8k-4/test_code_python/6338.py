def solution():
    """Lisa bought a new iPhone for $1000. She bought a phone contract that costs $200/month, a case that costs 20% of the cost of the phone, and headphones that cost half as much as the case. How much will Lisa spend on her phone in the first year?"""
    # Define the initial cost of the phone and the cost of the phone case
    phone_cost = 1000
    case_cost = phone_cost * 0.2

    # Define the cost of the headphones
    headphones_cost = case_cost / 2

    # Calculate the total cost of the phone and accessories
    total_cost = phone_cost + case_cost + headphones_cost

    # Calculate the total cost of the phone contract for a year
    contract_cost = 200 * 12

    # Calculate the total amount Lisa will spend on her phone in the first year
    total_spent = total_cost + contract_cost

    # Return the result
    result = total_spent
    return result

print(solution())