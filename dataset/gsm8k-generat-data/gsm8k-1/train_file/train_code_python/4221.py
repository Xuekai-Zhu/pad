def solution():
    """Tania has five baskets containing a total of 58 fruits. There are 18 mangoes in one basket, 10 pears in another, 
    12 pawpaws in another and the last 2 contain the same number of kiwi and lemon respectively, how many lemons are there?"""
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