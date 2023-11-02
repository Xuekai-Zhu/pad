def solution():
    num_women = 60
    married_women_ratio = 3/4
    single_men_ratio = 3/4

    # Calculate the number of married women and their husbands
    num_married_women = num_women * married_women_ratio
    num_husbands = num_married_women

    # Calculate the total number of men at the party
    num_men = num_husbands / married_women_ratio

    # Calculate the number of single men
    num_single_men = num_men * single_men_ratio

    # Calculate the total number of people at the party
    total_people = num_women + num_husbands + num_single_men
    result = total_people
    return result

print(solution())