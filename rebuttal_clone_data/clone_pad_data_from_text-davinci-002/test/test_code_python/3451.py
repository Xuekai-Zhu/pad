def solution():
    horses = 25
    feedings_per_day = 2
    days = 60
    pounds_per_feeding = 20
    pounds_per_bag = 1000
    total_pounds_needed = horses * feedings_per_day * days * pounds_per_feeding
    total_bags_needed = total_pounds_needed / pounds_per_bag
    result = total_bags_needed
    
    return result

print(solution())