def solution():
    
    initial_flowers = 2 * 5
    grown_flowers = initial_flowers + 20
    dead_flowers = 10
    remaining_flowers = grown_flowers - dead_flowers
    baskets = 5
    flowers_per_basket = remaining_flowers // baskets
    result = flowers_per_basket
    return result

print(solution())