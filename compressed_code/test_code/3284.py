def solution():
    
    total_fruits = 58
    mangoes = 18
    pears = 10
    pawpaws = 12
    lemons_kiwis = total_fruits - mangoes - pears - pawpaws
    kiwis = lemons_kiwis // 2
    lemons = lemons_kiwis - kiwis
    result = lemons
    return result

print(solution())