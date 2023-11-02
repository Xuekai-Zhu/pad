def solution():
    
    current_funds = 200
    target_funds = 1000
    avg_fund_per_person = 10
    total_funds_needed = target_funds - current_funds
    num_people_needed = total_funds_needed / avg_fund_per_person
    result = num_people_needed
    return result

print(solution())