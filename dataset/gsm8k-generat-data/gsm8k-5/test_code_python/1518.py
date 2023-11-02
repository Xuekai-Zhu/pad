def solution():
    total_cupcakes = 80  # A total of 80 cupcakes were ordered
    gluten_free_cupcakes = total_cupcakes // 2  # Half of the cupcakes are gluten-free
    non_gluten_free_cupcakes = total_cupcakes - gluten_free_cupcakes  # The rest of the cupcakes contain gluten

    # Calculate the number of vegan cupcakes that are also gluten-free
    vegan_cupcakes = 24  # There are 24 vegan cupcakes
    gluten_free_vegan_cupcakes = vegan_cupcakes // 2  # Half of the vegan cupcakes are gluten-free
    non_gluten_free_vegan_cupcakes = vegan_cupcakes - gluten_free_vegan_cupcakes  # The rest of the vegan cupcakes contain gluten

    # Calculate the number of non-vegan cupcakes that also contain gluten
    non_vegan_gluten_free_cupcakes = non_gluten_free_cupcakes - non_gluten_free_vegan_cupcakes

    result = non_vegan_gluten_free_cupcakes
    return result

print(solution())