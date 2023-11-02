def solution():
    """Amy is collecting candy for the car pool. She has 5 chocolate bars, 7 times as many M&Ms as chocolate bars, and 6 times as many marshmallows as M&Ms. Amy then arranges the candies into baskets. If she fills each basket with 10 candies, how many baskets will Amy fill?"""
    # Define the number of chocolate bars
    chocolate_bars = 5

    # Define the number of M&Ms, which is 7 times the number of chocolate bars
    mms = 7 * chocolate_bars

    # Define the number of marshmallows, which is 6 times the number of M&Ms
    marshmallows = 6 * mms

    # Calculate the total number of candies
    total_candies = chocolate_bars + mms + marshmallows

    # Calculate the number of baskets Amy can fill, assuming each basket has 10 candies
    baskets = total_candies // 10

    # Display the number of baskets Amy will fill
    result = baskets
    return result

print(solution())