def solution():
    # Calculate the total number of pairs of leggings needed for Haleigh's pets
    num_dog_legs = 4 * 4  # each dog has 4 legs
    num_cat_legs = 3 * 4  # each cat has 4 legs
    total_legs = num_dog_legs + num_cat_legs  # total number of legs
    num_leggings = total_legs // 2  # each pair of leggings covers 2 legs
    result = num_leggings
    return result

print(solution())