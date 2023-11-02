def solution():
    """Rose is out picking flowers for a vase she wants to fill. She starts off by picking 3 flowers with 5 petals each. She then picks 4 flowers with 6 petals each. She then adds another 5 flowers with 4 petals each. Lastly she picks 6 flowers with 7 petals each. As she's carrying these flowers over to fill the vase, she drops 1 of each and the wind blows them away. She puts the remaining flowers in the vase. How many petals in total are on the flowers in the vase?"""
    flowers = [3*5, 4*6, 5*4, 6*7]
    dropped_flowers = 4
    dropped_petals = dropped_flowers
    total_petals = sum(flowers) - dropped_petals
    result = total_petals
    return result

print(solution())