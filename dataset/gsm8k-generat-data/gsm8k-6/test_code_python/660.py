def solution():
    # Calculate the number of ants each child finds
    Abe_ants = 4
    Beth_ants = Abe_ants * 1.5  # 50% more ants than Abe
    CeCe_ants = Abe_ants * 2  # twice as many ants as Abe
    Duke_ants = Abe_ants / 2  # half as many ants as Abe

    # Calculate the total number of ants found by all four children
    total_ants = Abe_ants + Beth_ants + CeCe_ants + Duke_ants
    result = total_ants
    return result

print(solution())