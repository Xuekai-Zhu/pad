def solution():
    """The average number of fruits per basket in five baskets is 25. If basket A contains 15 apples, B has 30 mangoes, C has 20 peaches, D has 25 pears and E has some bananas, how many bananas are in basket E?"""
    total_fruits = 25 * 5
    fruits_in_other_baskets = 15 + 30 + 20 + 25
    bananas_in_basket_E = total_fruits - fruits_in_other_baskets
    result = bananas_in_basket_E
    return result

print(solution())