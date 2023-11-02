def solution():
    """A mum ordered 80 cupcakes for her daughter's birthday. Half of them are gluten-free. There are 24 vegan cupcakes and half of them are also gluten-free.  How many are non-vegan cupcakes that also contain gluten?"""
    # Define the total number of cupcakes and the number of gluten-free cupcakes
    total_cupcakes = 80
    gluten_free_cupcakes = total_cupcakes // 2

    # Calculate the number of non-vegan cupcakes
    non_vegan_cupcakes = total_cupcakes - 24

    # Calculate the number of non-vegan and gluten-free cupcakes
    non_vegan_gluten_free_cupcakes = gluten_free_cupcakes // 2

    # Calculate the final answer
    answer = non_vegan_gluten_free_cupcakes

    # Display the answer
    result = answer
    return result

print(solution())