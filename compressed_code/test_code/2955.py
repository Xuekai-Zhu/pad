def solution():
    
    num_family_members = 4
    join_fee = 4000
    monthly_cost = 1000
    total_cost = (num_family_members * join_fee) + (12 * num_family_members * monthly_cost)
    john_cost = total_cost / 2
    result = john_cost
    return result

print(solution())