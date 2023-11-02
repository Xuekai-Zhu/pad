def solution():
    # Calculate the number of adult women skeletons and their total bone count
    adult_women_count = 20 // 2
    adult_women_bones = adult_women_count * 20

    # Calculate the number of adult men skeletons and their total bone count
    adult_men_count = (20 - adult_women_count) // 2
    adult_men_bones = adult_men_count * (20 + 5)

    # Calculate the number of child skeletons and their total bone count
    child_count = 20 - adult_women_count - adult_men_count
    child_bones = child_count * (20//2)

    # Calculate the total number of bones in the graveyard
    total_bones = adult_women_bones + adult_men_bones + child_bones

    result = total_bones
    return result

print(solution())