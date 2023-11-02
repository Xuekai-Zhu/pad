def solution():
    phone_cost = 1000
    contract_cost = 200
    case_cost = 0.2 * phone_cost
    headphone_cost = 0.5 * case_cost
    num_months = 12

    # Calculate the total cost of the phone and accessories
    total_cost = phone_cost + case_cost + headphone_cost

    # Calculate the total cost of the phone contract for the first year
    total_contract_cost = contract_cost * num_months

    # Calculate the total cost for the first year
    total_spent = total_cost + total_contract_cost
    result = total_spent
    return result

print(solution())