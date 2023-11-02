def solution():
    num_chocolate_bars = 5
    num_MMs = num_chocolate_bars * 7
    num_marshmallows = num_MMs * 6
    total_candies = num_chocolate_bars + num_MMs + num_marshmallows
    candies_per_basket = 10
    num_baskets = total_candies // candies_per_basket
    result = num_baskets
    return result

print(solution())