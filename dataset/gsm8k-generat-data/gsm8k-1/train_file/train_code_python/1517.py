def solution():
    """A mum ordered 80 cupcakes for her daughter's birthday. Half of them are gluten-free. There are 24 vegan cupcakes and half of them are also gluten-free. How many are non-vegan cupcakes that also contain gluten?"""
    total_cupcakes = 80
    gluten_free = total_cupcakes / 2
    vegan_cupcakes = 24
    vegan_gluten_free = vegan_cupcakes / 2
    non_vegan_gluten_free = gluten_free - vegan_gluten_free
    result = non_vegan_gluten_free
    return result

print(solution())