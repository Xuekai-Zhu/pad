def solution():
    """Michael has 36 pets. 25% of them are dogs, 50% are cats, and the rest are bunnies. How many bunnies does he have?"""
    total_pets = 36
    dogs = total_pets * 0.25
    cats = total_pets * 0.50
    bunnies = total_pets - dogs - cats
    result = bunnies
    return result

print(solution())