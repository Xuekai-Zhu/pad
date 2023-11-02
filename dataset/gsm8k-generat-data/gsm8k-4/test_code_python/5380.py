def solution():
    """Hugh had eight pounds of candy, Tommy had six pounds of candy, and Melany had seven pounds of candy. If they share the candy equally, how much will each person have?"""
    # Define the initial amount of candy each person has
    hugh_candy = 8
    tommy_candy = 6
    melany_candy = 7

    # Calculate the total amount of candy
    total_candy = hugh_candy + tommy_candy + melany_candy

    # Calculate the amount of candy each person will have if they share equally
    each_person_candy = total_candy / 3

    # Return the result
    result = each_person_candy
    return result

print(solution())