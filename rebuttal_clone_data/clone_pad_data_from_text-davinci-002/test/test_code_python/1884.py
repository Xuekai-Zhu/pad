def solution():
    distance = 20
    speed = 10
    cost_per_hour = 30
    flat_fee = 20
    hours = distance / speed
    total_cost = cost_per_hour * hours + flat_fee
    result = total_cost
    return result

print(solution())