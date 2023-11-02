def solution():
    barrels = 4
    gallons_per_barrel = 7
    flow_rate = 3.5
    minutes_to_fill = (barrels * gallons_per_barrel) / flow_rate
    result = minutes_to_fill
    return result

print(solution())