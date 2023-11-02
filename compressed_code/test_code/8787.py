def solution():
    
    num_family_members = 4
    join_fee_per_person = 4000
    monthly_cost_per_person = 1000
    num_months_in_year = 12
    total_cost_per_person = join_fee_per_person + (monthly_cost_per_person * num_months_in_year)
    total_cost_for_family = total_cost_per_person * num_family_members
    john_pays = total_cost_for_family / 2
    result = john_pays
    return result

print(solution())