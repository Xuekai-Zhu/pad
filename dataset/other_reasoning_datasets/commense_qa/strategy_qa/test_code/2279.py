def solution():
    chinchilla = "rodent"
    felis_catus = "cat"
    chinchilla_cat_breed = "Persian"
    # Check if the Chinchilla breed of cats is named after the rodent or just shares a similar coat
    if chinchilla in chinchilla_cat_breed:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())