def solution():
    # Calculate the total number of female hippos
    total_hippo_females = int(35 * 5/7)

    # Calculate the number of new baby hippos born
    new_baby_hippos = total_hippo_females * 5

    # Calculate the number of newborn elephants
    num_newborn_elephants = 10 + new_baby_hippos

    # Calculate the new total number of elephants and hippos
    new_total_elephants = 20 + num_newborn_elephants
    new_total_hippos = 35 + new_baby_hippos

    # Calculate the total number of animals
    total_animals = new_total_elephants + new_total_hippos
    result = total_animals
    return result

print(solution())