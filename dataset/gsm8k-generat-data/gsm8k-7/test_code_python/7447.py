def solution():
    num_cats = 15
    cats_adopted = num_cats / 3
    cats_replaced = 2 * cats_adopted
    num_cats_remaining = num_cats - cats_adopted + cats_replaced
    num_dogs = 2 * num_cats_remaining
    total_animals = num_cats_remaining + num_dogs
    result = total_animals
    return result

print(solution())