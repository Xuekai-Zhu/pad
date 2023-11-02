def solution():
    """Tania has five baskets containing a total of 58 fruits. There are 18 mangoes in one basket, 10 pears in another, 12 pawpaws in another and the last 2 contain the same number of kiwi and lemon respectively, how many lemons are there?"""
    # Define the number of fruits in each basket
    mangoes = 18
    pears = 10
    pawpaws = 12
    kiwi = None
    lemons = None

    # Calculate the total number of fruits in the first three baskets
    total_fruits = mangoes + pears + pawpaws

    # Calculate the total number of fruits in all five baskets and find the difference
    difference = 58 - total_fruits

    # Divide the difference by 2 to get the number of kiwi and lemons in each of the last two baskets
    kiwi = difference // 2
    lemons = difference // 2

    # Display the number of lemons
    result = lemons
    return result

print(solution())