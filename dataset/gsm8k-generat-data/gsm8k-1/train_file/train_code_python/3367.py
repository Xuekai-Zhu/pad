def solution():
    """Lilibeth and her friends go strawberry picking. Lilibeth fills 6 baskets where each basket holds 50 strawberries. If three of Lilibeth's friends pick the same amount as her, how many strawberries do Lilibeth and her friends pick in all?"""
    strawberries_per_basket = 50
    lilibeth_baskets = 6
    lilibeth_total = strawberries_per_basket * lilibeth_baskets
    friends_total = lilibeth_total * 3
    result = lilibeth_total + friends_total
    return result

print(solution())