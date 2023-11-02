def solution():
    """Tania has five baskets containing a total of 58 fruits. There are 18 mangoes in one basket, 10 pears in another, 12 pawpaws in another and the last 2 contain the same number of kiwi and lemon respectively, how many lemons are there?"""
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