def solution():
    """Cindy and Olaf made 15 candied apples which they will be selling for $2 each, and 12 candied grapes which they will be selling for $1.5. How much will they earn if they sell everything?"""
    apples = 15
    apple_price = 2
    grapes = 12
    grape_price = 1.5
    total_apple_revenue = apples * apple_price
    total_grape_revenue = grapes * grape_price
    total_revenue = total_apple_revenue + total_grape_revenue
    result = total_revenue
    return result

print(solution())