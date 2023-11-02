def solution():
    abe = 4  # Abe finds 4 ants
    beth = abe * 1.5  # Beth sees 50% more ants than Abe
    cece = abe * 2  # CeCe watches twice as many ants as Abe
    duke = abe / 2  # Duke discovers half as many ants as Abe

    # Calculate the total number of ants found by the four children together
    total_ants = abe + beth + cece + duke
    result = total_ants
    return result

print(solution())