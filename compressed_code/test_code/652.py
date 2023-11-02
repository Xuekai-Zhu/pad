def solution():
    
    total_acorns = 575
    num_squirrels = 5
    acorns_per_squirrel = 130
    needed_acorns = (num_squirrels * acorns_per_squirrel) - total_acorns
    acorns_per_squirrel_needed = needed_acorns / num_squirrels
    result = acorns_per_squirrel_needed
    return result

print(solution())