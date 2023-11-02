def solution():
    
    strawberries_per_basket = 50
    lilibeth_baskets = 6
    lilibeth_total = strawberries_per_basket * lilibeth_baskets
    friends_total = lilibeth_total * 3
    result = lilibeth_total + friends_total
    return result

print(solution())