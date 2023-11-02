def solution():
    num_men = 2
    num_women = 3
    men_apples = 30
    women_apples = men_apples + 20

    # Calculate the total number of apples bought by the two men
    total_men_apples = num_men * men_apples

    # Calculate the total number of apples bought by the three women
    total_women_apples = num_women * women_apples

    # Calculate the total number of apples bought
    total_apples = total_men_apples + total_women_apples
    result = total_apples
    return result

print(solution())