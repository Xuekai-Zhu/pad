def solution():
    # Calculate the number of gluten-free cupcakes
    gf_cupcakes = 80/2  # Half of the cupcakes are gluten-free
    gf_vegan_cupcakes = 24/2  # Half of the vegan cupcakes are gluten-free
    non_vegan_gf_cupcakes = gf_cupcakes - gf_vegan_cupcakes  # Number of non-vegan gluten-free cupcakes

    result = non_vegan_gf_cupcakes
    return result

print(solution())