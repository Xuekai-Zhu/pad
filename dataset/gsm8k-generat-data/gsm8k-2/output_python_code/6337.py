def solution():
    """Lisa bought a new iPhone for $1000. She bought a phone contract that costs $200/month, a case that costs 20% of the cost of the phone, and headphones that cost half as much as the case. How much will Lisa spend on her phone in the first year?"""
    phone_cost = 1000
    case_cost = 0.2 * phone_cost
    headphone_cost = 0.5 * case_cost
    total_accessories_cost = case_cost + headphone_cost
    contract_cost_per_year = 200 * 12
    total_cost = phone_cost + total_accessories_cost + contract_cost_per_year
    result = total_cost
    return result

print(solution())