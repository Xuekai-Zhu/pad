def solution():
    # Calculate the number of married women
    married_women = int(0.75 * 60)

    # Calculate the number of men at the party
    men = married_women

    # Calculate the number of single men
    single_men = int(0.75 * men)

    # Calculate the total number of people at the party
    total_people = 60 + married_women + men + single_men

    result = total_people
    return result

print(solution())