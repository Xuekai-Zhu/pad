def solution():
    kobe_animal_product = "Kobe beef"
    blt_animal_product = "bacon"
    # Check if Kobe's animal product is used in a BLT
    if kobe_animal_product.lower() in blt_animal_product.lower():
        result = "yes"
    else:
        result = "no"
    return result

print(solution())