def solution():
    """Lilibeth and her friends go strawberry picking. Lilibeth fills 6 baskets where each basket holds 50 strawberries. If three of Lilibeth's friends pick the same amount as her, how many strawberries do Lilibeth and her friends pick in all?"""
    lilibeth_baskets = 6
    friends = 3
    strawberries_per_basket = 50
    total_strawberries = (lilibeth_baskets + (friends * lilibeth_baskets)) * strawberries_per_basket
    result = total_strawberries
    return result

print(solution())