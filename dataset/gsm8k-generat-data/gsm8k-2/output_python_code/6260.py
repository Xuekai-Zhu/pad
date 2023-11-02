def solution():
    """At the same store, Peter bought 2 pairs of pants and 5 shirts for $62 total, and Jessica bought 2 shirts for $20 total. Each pair of pants cost the same price, and each shirt cost the same price. How much does 1 pair of pants cost?"""
    pants_price = 0
    shirt_price = 0
    for i in range(1, 63):
        for j in range(1, 63):
            if (2*i + 5*j == 62) and (2*j == 20):
                pants_price = i
                shirt_price = j
    result = pants_price
    return result

print(solution())