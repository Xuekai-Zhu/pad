def solution():
    """There are ten more newborn elephants than baby hippos. If an entire herd starts with 20 elephants and 35 hippos, and the female hippos, whose number is 5/7 of the total number of hippos, give birth to 5 new baby hippos each, find the number of animals that are there altogether?"""
    initial_elephants = 20
    initial_hippos = 35
    new_hippos_per_female = 5
    female_hippos = initial_hippos * (5/7)
    total_new_hippos = female_hippos * new_hippos_per_female
    total_hippos = initial_hippos + total_new_hippos
    newborn_elephants = total_hippos + 10
    total_animals = initial_elephants + newborn_elephants + total_hippos
    result = total_animals
    return result

print(solution())