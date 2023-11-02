def solution():
    """John joins a country club with 3 other members of his family. The fee to join is $4000 per person. There is also a monthly cost of $1000 per person. John pays half the cost. How much does John pay for the first year?"""
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