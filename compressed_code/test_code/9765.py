def solution():
    
    homes = 3
    length = 100
    width = 100
    height = .5
    density = 150
    cost_per_pound = .02
    volume = length * width * height
    total_volume = volume * homes
    total_weight = total_volume * density
    cost = total_weight * cost_per_pound
    result = cost
    return result

print(solution())