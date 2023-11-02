def solution():
    # Find the total number of pants and dresses bought by Alexis
    alexis_pants = 21
    alexis_dresses = 18
    total_alexis = alexis_pants + alexis_dresses

    # Find how many times more pants and dresses Alexis bought than Isabella
    ratio = total_alexis / (3+1)

    # Find the total number of pants and dresses bought by Isabella
    total_isabella = ratio * 1

    result = total_isabella + total_alexis
    return result

print(solution())