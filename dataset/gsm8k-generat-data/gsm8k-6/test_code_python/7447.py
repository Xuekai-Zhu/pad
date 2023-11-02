def solution():
    # Calculate the number of cats adopted and remaining in the shelter
    adopted_cats = 15 // 3
    remaining_cats = 15 - adopted_cats
    new_cats = adopted_cats * 2
    final_cat_count = remaining_cats + new_cats

    # Calculate the total number of animals in the shelter
    total_animals = final_cat_count + final_cat_count * 2
    result = total_animals
    return result

print(solution())