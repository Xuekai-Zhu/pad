def solution():
    
    total_bags = 80
    doritos_percentage = 0.25
    doritos_bags = total_bags * doritos_percentage
    piles = 4
    bags_per_pile = doritos_bags / piles
    result = bags_per_pile
    return result

print(solution())