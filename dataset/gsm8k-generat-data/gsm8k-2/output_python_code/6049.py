def solution():
    """Haleigh needs to buy leggings for her pet animals. She has 4 dogs and 3 cats. How many pairs of leggings does she need?"""
    total_legs = 4*4 + 3*4 # Each dog has 4 legs and each cat has 4 legs
    pairs_leggings = total_legs // 2 # Each pair of leggings covers 2 legs
    result = pairs_leggings
    return result

print(solution())