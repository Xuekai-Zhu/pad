def solution():
    """Amy is collecting candy for the car pool. She has 5 chocolate bars, 7 times as many M&Ms as chocolate bars, and 6 times as many marshmallows as M&Ms. Amy then arranges the candies into baskets. If she fills each basket with 10 candies, how many baskets will Amy fill?"""
    # Calculate the number of M&Ms
    mms = 7 * 5

    # Calculate the number of marshmallows
    marshmallows = 6 * mms

    # Calculate the total number of candies
    total_candies = 5 + mms + marshmallows

    # Calculate the number of baskets
    baskets = total_candies // 10

    result = baskets
    return result

print(solution())