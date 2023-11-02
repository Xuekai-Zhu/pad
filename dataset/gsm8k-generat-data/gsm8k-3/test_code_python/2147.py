def solution():
    """There are ten more newborn elephants than baby hippos. If an entire herd starts with 20 elephants and 35 hippos, and the female hippos, whose number is 5/7 of the total number of hippos, give birth to 5 new baby hippos each, find the number of animals that are there altogether?"""
    # Define the initial number of elephants and hippos
    initial_elephants = 20
    initial_hippos = 35

    # Calculate the total number of hippos including the newborns
    female_hippos = (5/7) * initial_hippos
    baby_hippos = 5 * female_hippos
    total_hippos = initial_hippos + baby_hippos

    # Calculate the total number of elephants including the newborns
    total_elephants = initial_elephants + (total_hippos + 10)

    # Calculate the total number of animals
    total_animals = total_elephants + total_hippos

    # Display the total number of animals
    result = total_animals
    return result

print(solution())