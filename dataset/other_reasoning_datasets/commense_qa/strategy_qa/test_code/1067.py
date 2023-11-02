def solution():
    venture_annual_fee = 95
    church_membership_fee = 225
    years_as_venture_member = 5
    venture_total_cost = venture_annual_fee * years_as_venture_member
    if venture_total_cost < church_membership_fee:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())