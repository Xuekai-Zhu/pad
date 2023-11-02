def solution():
    women = 60  # There were 60 women at the party
    married_women = (3/4) * women  # Three-fourths of the women were married
    husbands = married_women  # Each married woman brought her husband to the party
    single_men = (3/4) * husbands  # Three-fourths of the men at the party were single

    # Calculate the total number of people at the party
    total_people = women + husbands + single_men
    result = total_people
    return result

print(solution())