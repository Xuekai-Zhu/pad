def solution():
    """A mum ordered 80 cupcakes for her daughter's birthday. Half of them are gluten-free. There are 24 vegan cupcakes and half of them are also gluten-free. How many are non-vegan cupcakes that also contain gluten?"""
    # Define the total number of cupcakes
    total_cupcakes = 80

    # Calculate the number of gluten-free cupcakes
    gluten_free_cupcakes = total_cupcakes / 2

    # Calculate the number of non-gluten-free cupcakes
    non_gluten_free_cupcakes = total_cupcakes - gluten_free_cupcakes

    # Calculate the number of vegan cupcakes that are also gluten-free
    vegan_gluten_free_cupcakes = 24 / 2

    # Calculate the number of non-vegan cupcakes that are also gluten-free
    non_vegan_gluten_free_cupcakes = gluten_free_cupcakes - vegan_gluten_free_cupcakes

    result = non_vegan_gluten_free_cupcakes
    return result

print(solution())