def solution():
    """Jezebel needs to buy two dozens of red roses and 3 pieces of sunflowers for a bouquet that she is going to arrange. Each red rose costs $1.50 and each sunflower costs $3. How much will Jezebel pay for all those flowers?"""
    red_roses = 2 * 12
    red_roses_cost = red_roses * 1.5
    sunflowers_cost = 3 * 3
    total_cost = red_roses_cost + sunflowers_cost
    result = total_cost
    return result

print(solution())