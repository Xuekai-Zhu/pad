def solution():
    
    chocolate_bars = 5
    mms = 7 * chocolate_bars
    marshmallows = 6 * mms
    total_candies = chocolate_bars + mms + marshmallows
    baskets = total_candies // 10
    result = baskets
    return result

print(solution())