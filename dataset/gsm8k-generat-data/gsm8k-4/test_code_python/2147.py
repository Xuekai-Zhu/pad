def solution():
    """There are ten more newborn elephants than baby hippos. If an entire herd starts with 20 elephants and 35 hippos, and the female hippos, whose number is 5/7 of the total number of hippos, give birth to 5 new baby hippos each, find the number of animals that are there altogether?"""
    # Define the initial number of elephants and hippos
    initial_elephants = 20
    initial_hippos = 35

    # Calculate the number of female hippos and the number of newborn hippos
    female_hippos = int(initial_hippos * 5 / 7)
    newborn_hippos = female_hippos * 5

    # Calculate the number of baby hippos and elephants
    baby_hippos = newborn_hippos - 10
    baby_elephants = baby_hippos + 10

    # Calculate the total number of animals
    total_animals = initial_elephants + initial_hippos + baby_hippos + baby_elephants

    # return the result
    result = total_animals
    return result

print(solution())