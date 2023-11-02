def solution():
    """Amy is collecting candy for the car pool. She has 5 chocolate bars, 7 times as many M&Ms as chocolate bars, and 6 times as many marshmallows as M&Ms. Amy then arranges the candies into baskets. If she fills each basket with 10 candies, how many baskets will Amy fill?"""
    chocolate_bars = 5
    mms = 7 * chocolate_bars
    marshmallows = 6 * mms
    total_candies = chocolate_bars + mms + marshmallows
    candies_per_basket = 10
    baskets_filled = total_candies // candies_per_basket
    result = baskets_filled
    return result

print(solution())