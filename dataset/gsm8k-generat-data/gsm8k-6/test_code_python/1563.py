def solution():
    # Calculate the number of cows Aaron has
    cows_Matthews = 60
    cows_Aaron = 4 * cows_Matthews

    # Calculate the number of cows Marovich has
    cows_Marovich = (cows_Matthews + cows_Aaron) - 30

    # Calculate the total number of cows they have altogether
    total_cows = cows_Matthews + cows_Aaron + cows_Marovich
    result = total_cows
    return result

print(solution())