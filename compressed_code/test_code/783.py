def solution():
    
    sugar_ratio = 1
    cream_cheese_ratio = 4
    vanilla_ratio = 0.5
    egg_ratio = 2
    sugar_used = 2
    cream_cheese_used = sugar_used * cream_cheese_ratio / sugar_ratio
    vanilla_used = cream_cheese_used * vanilla_ratio
    egg_used = vanilla_used * egg_ratio
    result = egg_used
    return result

print(solution())