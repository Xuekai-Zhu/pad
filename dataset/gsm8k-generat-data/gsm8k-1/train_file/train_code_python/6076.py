def solution():
    """Jezebel needs to buy two dozens of red roses and 3 pieces of sunflowers for a bouquet that she is going to arrange. Each red rose costs $1.50 and each sunflower costs $3. How much will Jezebel pay for all those flowers?"""
    red_roses = 24 # Two dozens of roses
    sunflowers = 3
    red_roses_price = 1.5
    sunflowers_price = 3
    total_cost = (red_roses * red_roses_price) + (sunflowers * sunflowers_price)
    result = total_cost
    return result

print(solution())