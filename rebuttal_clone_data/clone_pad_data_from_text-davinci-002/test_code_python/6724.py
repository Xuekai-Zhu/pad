def solution():
    apples = 9
    oranges = 15
    bananas = 14
    fruits_per_basket = apples + oranges + bananas
    num_baskets = 4
    total_fruits = (fruits_per_basket * 3) + (fruits_per_basket - 2)
    result = total_fruits
    return result

print(solution())