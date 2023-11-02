def solution():
    
    total_fruits = 58
    mangoes = 18
    pears = 10
    pawpaws = 12
    kiwi_lemon_baskets = 2
    kiwi_lemon = (total_fruits - (mangoes + pears + pawpaws)) / kiwi_lemon_baskets
    lemons = kiwi_lemon
    result = lemons
    return result

print(solution())