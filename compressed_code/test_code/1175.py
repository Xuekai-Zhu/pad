def solution():
    
    total_cupcakes = 80
    gluten_free_cupcakes = total_cupcakes / 2
    vegan_cupcakes = 24
    gluten_free_vegan_cupcakes = vegan_cupcakes / 2
    non_vegan_gluten_free_cupcakes = gluten_free_cupcakes - gluten_free_vegan_cupcakes
    result = non_vegan_gluten_free_cupcakes
    return result

print(solution())