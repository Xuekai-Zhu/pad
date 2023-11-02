def solution():
    """Michael has 2 cats and 3 dogs. He needs to pay a friend to watch them, who charges $13 a night per animal. How much does Michael have to pay?"""
    cats = 2
    dogs = 3
    price_per_animal = 13
    total_nights = 7  # assuming one week of pet-sitting
    total_cost = (cats + dogs) * price_per_animal * total_nights
    result = total_cost
    return result

print(solution())