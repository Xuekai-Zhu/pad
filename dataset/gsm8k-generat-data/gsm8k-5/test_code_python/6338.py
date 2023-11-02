def solution():
    phone_cost = 1000  # Lisa bought a new iPhone for $1000
    contract_cost = 200 * 12  # Lisa's phone contract costs $200 per month for 12 months
    case_cost = phone_cost * 0.2  # Lisa's phone case costs 20% of the cost of the phone
    headphone_cost = case_cost / 2  # Lisa's headphones cost half as much as the phone case

    # Calculate the total cost of Lisa's phone in the first year
    total_cost = phone_cost + contract_cost + case_cost + headphone_cost
    result = total_cost
    return result

print(solution())