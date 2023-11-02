def solution():
    """Haleigh needs to buy leggings for her pet animals. She has 4 dogs and 3 cats. How many pairs of leggings does she need?"""
    # Define the number of animals and legs
    num_dogs = 4
    num_cats = 3
    legs_per_animal = 4

    # Calculate the total number of legs
    total_legs = (num_dogs + num_cats) * legs_per_animal

    # Calculate the number of pairs of leggings needed
    num_leggings = total_legs // 2

    result = num_leggings
    return result

print(solution())