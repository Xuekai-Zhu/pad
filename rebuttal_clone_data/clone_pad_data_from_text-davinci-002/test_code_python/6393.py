def solution():
    shirts = 18
    pants = 12
    sweaters = 17
    jeans = 13
    total_clothes = shirts + pants + sweaters + jeans
    washing_machine_capacity = 15
    cycles_required = total_clothes // washing_machine_capacity
    if total_clothes % washing_machine_capacity > 0:
        cycles_required = cycles_required + 1
    minutes_per_cycle = 45
    total_minutes = cycles_required * minutes_per_cycle
    hours = total_minutes // 60
    if total_minutes % 60 > 0:
        hours = hours + 1
    result = hours
    return result

print(solution())