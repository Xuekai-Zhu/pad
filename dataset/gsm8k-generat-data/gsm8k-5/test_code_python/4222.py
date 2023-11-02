def solution():
    total_fruits = 58  # There are 58 fruits in total
    mangoes = 18  # There are 18 mangoes in one basket
    pears = 10  # There are 10 pears in another basket
    pawpaws = 12  # There are 12 pawpaws in another basket

    # Calculate the total number of fruits in the two remaining baskets
    remaining_fruits = total_fruits - mangoes - pears - pawpaws

    # Since the two remaining baskets contain the same number of kiwi and lemon, we can assume that the number of lemon is half of the remaining fruits
    lemons = remaining_fruits / 2
    result = lemons
    return result

print(solution())