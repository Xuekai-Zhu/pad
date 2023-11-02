def solution():
    """Dave bought a large pack of french fries and ate fourteen before a hungry seagull stole the pack out of his hand. When the seagull landed, he gobbled down half the amount of french fries that Dave ate. Then three pigeons bullied him away from the food, and each pigeon ate three fries. Later, a raccoon stole two thirds of the remaining fries. Ants carried off a final french fry, leaving five behind. How many french fries were in the pack when Dave bought it?"""
    initial_amount = ((14*2) + (3*3) + 5) / (1/2) * (3/3) * (3/2)
    result = initial_amount
    return result

print(solution())