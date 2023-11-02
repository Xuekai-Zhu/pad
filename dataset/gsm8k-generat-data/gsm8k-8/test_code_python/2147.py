def solution():
    # Calculate the number of female hippos
    female_hippos = 5/7 * 35

    # Calculate the number of baby hippos born
    baby_hippos = 5 * female_hippos

    # Calculate the number of newborn elephants
    newborn_elephants = 10 + baby_hippos

    # Calculate the total number of animals
    total_animals = 20 + newborn_elephants + 35 + baby_hippos

    result = total_animals
    return result

print(solution())