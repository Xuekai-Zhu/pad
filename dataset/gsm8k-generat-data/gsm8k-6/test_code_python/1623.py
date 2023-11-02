def solution():
    # Calculate the number of married women and their husbands who attended the party
    married_women = (3/4) * 60  
    married_husbands = married_women

    # Calculate the number of single men who attended the party
    total_men = (4/3) * married_husbands  # since 3/4 of the women were married and brought their husbands
    single_men = (3/4) * total_men  

    # Calculate the total number of people who attended the party
    total_people = 60 + married_husbands + single_men
    result = total_people
    return result

print(solution())