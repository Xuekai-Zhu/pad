def solution():
    """There were 60 women at the party, and three-fourths of these women were married and brought their husbands with them to the party. If 3/4 of the men at the party were single, how many people attended the party?"""
    women = 60
    married_women = 3/4 * women
    husbands = married_women
    single_men = 3/4 * husbands
    total_attendees = women + married_women + husbands + single_men
    result = total_attendees
    return result

print(solution())