def solution():
    wine_takers = 26
    soda_takers = 22
    both_takers = 17

    # Calculate the total number of people who took either wine or soda
    total_takers = wine_takers + soda_takers - both_takers

    # Calculate the total number of people who took both wine and soda
    # This count is subtracted from the total number of takers because they were already counted above
    num_both_takers = both_takers

    # Calculate the total number of people at the gathering
    total_people = total_takers + num_both_takers
    result = total_people
    return result

print(solution())