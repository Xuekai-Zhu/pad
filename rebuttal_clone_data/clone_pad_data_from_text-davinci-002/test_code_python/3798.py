def solution():
    joining_fee = 4000
    monthly_cost = 1000
    number_of_people = 4
    total_joining_cost = joining_fee * number_of_people
    total_monthly_cost = monthly_cost * number_of_people
    total_yearly_cost = total_joining_cost + (total_monthly_cost * 12)
    johns_share = total_yearly_cost / 2
    result = johns_share
    return result

print(solution())