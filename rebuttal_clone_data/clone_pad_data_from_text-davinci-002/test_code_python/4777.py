def solution():
 
    chairs = 8
    percent_off = 25
    additional_percent_off = 33.3
    cost_per_chair = 20
    total_percent_off = percent_off + additional_percent_off
    total_cost = chairs * cost_per_chair
    discounted_total_cost = total_cost - (total_cost * (total_percent_off / 100))
    result = discounted_total_cost
 
    return result

print(solution())