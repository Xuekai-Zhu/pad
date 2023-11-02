def solution():
    # Find the number of newborn elephants and baby hippos
    newborn_elephants = 10 + baby_hippos
    baby_hippos = 5 * (5/7) * 35  # female hippos give birth to 5 new baby hippos each

    # Update the total number of elephants and hippos
    total_elephants = 20 + newborn_elephants
    total_hippos = 35 + baby_hippos

    # Calculate the total number of animals
    total_animals = total_elephants + total_hippos
    result = total_animals
    return result

print(solution())