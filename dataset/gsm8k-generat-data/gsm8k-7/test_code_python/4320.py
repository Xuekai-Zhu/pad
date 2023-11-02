def solution():
    length = 6
    width = 3
    area = length * width
    paint_cost_per_meter = 4
    paint_cost = area * paint_cost_per_meter

    painting_rate = 1.5
    painting_cost_per_hour = 10
    total_painting_hours = area / painting_rate
    painting_cost = total_painting_hours * painting_cost_per_hour

    total_cost = paint_cost + painting_cost
    result = total_cost
    return result

print(solution())