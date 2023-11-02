def solution():
    chocolate_bars = 5  # Amy has 5 chocolate bars
    MMs = 7 * chocolate_bars  # Amy has 7 times as many M&Ms as chocolate bars
    marshmallows = 6 * MMs  # Amy has 6 times as many marshmallows as M&Ms

    # Calculate the total number of candies Amy has
    total_candies = chocolate_bars + MMs + marshmallows

    # Calculate the number of baskets Amy can fill
    baskets = total_candies // 10

    result = baskets
    return result

print(solution())