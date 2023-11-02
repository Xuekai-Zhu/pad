def solution():
    """Abe finds 4 ants on the sidewalk.  Beth sees 50% more ants than Abe.  CeCe watches twice as many ants as Abe.  Duke discovers half as many ants as Abe.  How many ants do the four children find together?"""
    # Define the number of ants each child finds
    abe_ants = 4
    beth_ants = abe_ants * 1.5
    cece_ants = abe_ants * 2
    duke_ants = abe_ants * 0.5

    # Calculate the total number of ants found
    total_ants = abe_ants + beth_ants + cece_ants + duke_ants

    # Display the total number of ants found
    result = total_ants
    return result

print(solution())