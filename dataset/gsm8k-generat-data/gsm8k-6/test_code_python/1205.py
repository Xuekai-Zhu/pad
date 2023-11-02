def solution():
    # Calculate the number of adult women skeletons in the graveyard
    adult_women = 20/2

    # Calculate the number of adult men skeletons in the graveyard
    adult_men = (20 - adult_women)/2

    # Calculate the number of children skeletons in the graveyard
    children = (20 - adult_women - adult_men)

    # Calculate the total number of bones in the graveyard
    total_bones = (adult_women * 20) + (adult_men * 25) + (children * 10)
    result = total_bones
    return result

print(solution())