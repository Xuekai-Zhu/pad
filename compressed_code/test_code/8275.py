def solution():
    
    chocolate_bars = 5
    mms = 7 * chocolate_bars
    marshmallows = 6 * mms
    total_candies = chocolate_bars + mms + marshmallows
    candies_per_basket = 10
    baskets_filled = total_candies // candies_per_basket
    result = baskets_filled
    return result

print(solution())