def solution():
    """Olly wants to get shoes to protect his pets’ paws. He owns 3 dogs, 2 cats, and a ferret. How many shoes does he need?"""
    dogs = 3
    cats = 2
    ferret = 1
    shoes_per_pet = 4
    total_pets = dogs + cats + ferret
    total_shoes = total_pets * shoes_per_pet
    result = total_shoes
    return result

print(solution())