def solution():
    """Abe finds 4 ants on the sidewalk.  Beth sees 50% more ants than Abe.  CeCe watches twice as many ants as Abe.  Duke discovers half as many ants as Abe.  How many ants do the four children find together?"""
    # Define the initial number of ants Abe found
    abe_ants = 4

    # Calculate the number of ants Beth found
    beth_ants = abe_ants * 1.5

    # Calculate the number of ants CeCe found
    cece_ants = abe_ants * 2

    # Calculate the number of ants Duke found
    duke_ants = abe_ants / 2

    # Calculate the total number of ants found by all children
    total_ants = abe_ants + beth_ants + cece_ants + duke_ants

    # return the result
    result = total_ants
    return result

print(solution())