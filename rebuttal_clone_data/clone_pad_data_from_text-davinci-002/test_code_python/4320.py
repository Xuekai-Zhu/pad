def solution():
    width = 6
    height = 3
    cost_per_square_meter = 4
    area = width * height
    cost = area * cost_per_square_meter
    meters_painted_per_hour = 1.5
    hours = area / meters_painted_per_hour
    hourly_rate = 10
    labor_cost = hours * hourly_rate
    total_cost = cost + labor_cost
    result = total_cost
    return result

print(solution())