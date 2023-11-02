def solution():
    total_cupcakes = 80
    num_gluten_free = total_cupcakes / 2
    num_vegan = 24
    num_gluten_free_vegan = num_vegan / 2

    # Calculate the number of non-vegan cupcakes that also contain gluten
    num_non_vegan_gluten_free = num_gluten_free - num_gluten_free_vegan
    result = num_non_vegan_gluten_free
    return result

print(solution())