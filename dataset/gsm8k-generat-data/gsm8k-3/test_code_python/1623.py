def solution():
    """There were 60 women at the party, and three-fourths of these women were married and brought their husbands with them to the party. If 3/4 of the men at the party were single, how many people attended the party?"""
    # Calculate the number of women who brought their husbands
    married_women = 60 * 0.75
    husbands = married_women * 1  # each married woman brought one husband

    # Calculate the total number of men at the party
    total_men = husbands / 0.25  # 1/4th of the men were husbands, so 3/4th must be single

    # Calculate the total number of people at the party
    total_people = 60 + husbands + total_men

    # Display the total number of people at the party
    result = total_people
    return result

print(solution())