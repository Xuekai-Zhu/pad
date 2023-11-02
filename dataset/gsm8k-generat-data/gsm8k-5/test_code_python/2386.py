def solution():
    initial_cats = 6  # Half of the cats the shelter already had
    newly_admitted_cats = 12  # Twelve cats were recently taken in
    cats_before_adoption = initial_cats + newly_admitted_cats  # Total number of cats before adoption
    cats_after_adoption = cats_before_adoption - 3  # Three cats were adopted
    cats_with_kittens = cats_after_adoption + 5  # The cat with kittens gives birth to five kittens
    remaining_cats = cats_with_kittens - 1  # One cat was picked up by its owner
    result = remaining_cats
    return result

print(solution())