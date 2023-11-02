def solution():
    """At the pet store, there are 7 puppies and 6 kittens for sale. Two puppies and three kittens are sold. How many pets remain at the store?"""
    total_pets = 7 + 6
    pets_sold = 2 + 3
    pets_remaining = total_pets - pets_sold
    result = pets_remaining
    return result

print(solution())