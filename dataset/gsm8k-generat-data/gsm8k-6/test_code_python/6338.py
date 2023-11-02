def solution():
    phone_cost = 1000  # cost of the phone
    contract_cost = 200 * 12  # cost of the phone contract for a year
    case_cost = 0.2 * phone_cost  # cost of the phone case
    headphone_cost = 0.5 * case_cost  # cost of the headphones
    total_cost = phone_cost + contract_cost + case_cost + headphone_cost  # total cost of the phone in the first year
    result = total_cost
    return result

print(solution())