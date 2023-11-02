def solution():
    """Tania has five baskets containing a total of 58 fruits. There are 18 mangoes in one basket, 10 pears in another, 12 pawpaws in another and the last 2 contain the same number of kiwi and lemon respectively, how many lemons are there?"""
    # Define the number of fruits in each basket
    mangoes = 18
    pears = 10
    pawpaws = 12

    # Calculate the total number of fruits in the first three baskets
    total_fruits = mangoes + pears + pawpaws

    # Calculate the total number of fruits in the last two baskets
    total_last_baskets = 58 - total_fruits

    # Define the number of kiwis in the fourth basket
    kiwis = int(total_last_baskets / 2)

    # Calculate the number of lemons in the fifth basket
    lemons = total_last_baskets - kiwis

    # Display the number of lemons
    result = lemons
    return result

print(solution())