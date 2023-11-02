def solution():
    total_fruits = 58
    mangoes = 18
    pears = 10
    pawpaws = 12
    kiwi = 0
    lemon = 0

    # Calculate the total fruits in the baskets containing kiwi and lemon combined
    kiwi_lemon_baskets = 5 - 3
    kiwi_lemon_fruits = total_fruits - mangoes - pears - pawpaws

    # Calculate the number of kiwi fruits
    kiwi = kiwi_lemon_fruits // 2

    # Calculate the number of lemon fruits
    lemon = kiwi_lemon_fruits // 2

    result = lemon
    return result

print(solution())