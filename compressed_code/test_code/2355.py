def solution():
    
    wednesday_harvest = 400
    thursday_harvest = wednesday_harvest / 2
    friday_harvest = 2000 - wednesday_harvest - thursday_harvest
    remaining_harvest = friday_harvest - 700
    result = remaining_harvest
    return result

print(solution())