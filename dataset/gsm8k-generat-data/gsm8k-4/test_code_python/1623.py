def solution():
    """There were 60 women at the party, and three-fourths of these women were married and brought their husbands with them to the party. If 3/4 of the men at the party were single, how many people attended the party?"""
    # Calculate the number of women who brought their husbands
    married_women = 60 * (3/4)
    husbands = married_women

    # Calculate the total number of men
    total_men = husbands / (3/4)

    # Calculate the number of single men
    single_men = total_men * (3/4)

    # Calculate the total number of people at the party
    total_people = 60 + husbands + single_men

    result = total_people
    return result

print(solution())