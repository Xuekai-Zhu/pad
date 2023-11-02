def solution():
    total_cupcakes = 80
    gf_cupcakes = total_cupcakes / 2
    vegan_cupcakes = 24
    gf_vegan_cupcakes = vegan_cupcakes / 2

    # Calculate the number of non-vegan cupcakes
    non_vegan_cupcakes = total_cupcakes - vegan_cupcakes

    # Calculate the number of non-vegan cupcakes that also contain gluten
    non_vegan_gf_cupcakes = gf_cupcakes - gf_vegan_cupcakes

    result = non_vegan_gf_cupcakes
    return result

print(solution())