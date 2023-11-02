def solution():
    phone_cost = 1000
    contract_cost = 200 * 12
    case_cost = 0.2 * phone_cost
    headphone_cost = 0.5 * case_cost

    total_cost = phone_cost + contract_cost + case_cost + headphone_cost
    result = total_cost
    return result

print(solution())