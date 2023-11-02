def solution():
    
    lilibeth_baskets = 6
    friends = 3
    strawberries_per_basket = 50
    total_strawberries = (lilibeth_baskets + (friends * lilibeth_baskets)) * strawberries_per_basket
    result = total_strawberries
    return result

print(solution())