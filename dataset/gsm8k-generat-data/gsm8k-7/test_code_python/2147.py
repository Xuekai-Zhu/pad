def solution():
    num_elephants = 20
    num_hippos = 35

    # Calculate the number of newborn elephants
    num_newborn_elephants = num_hippos + 10

    # Calculate the total number of hippos after giving birth
    num_female_hippos = int(5/7 * num_hippos)
    num_baby_hippos = num_female_hippos * 5
    total_hippos = num_hippos + num_baby_hippos

    # Calculate the total number of animals
    total_animals = num_elephants + total_hippos + num_newborn_elephants
    result = total_animals
    return result

print(solution())