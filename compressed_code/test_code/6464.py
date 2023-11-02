def solution():
    
    apple_trees = 30
    apple_production = 150
    peach_trees = 45
    peach_production = 65
    total_apple_production = apple_trees * apple_production
    total_peach_production = peach_trees * peach_production
    total_fruit_harvested = total_apple_production + total_peach_production
    result = total_fruit_harvested
    
    return result

print(solution())