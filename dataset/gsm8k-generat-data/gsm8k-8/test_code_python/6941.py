def solution():
    # Calculate the number of children present
    num_children = 80

    # Calculate the number of male adults present
    num_male_adults = 60

    # Calculate the total number of adults present
    num_adults = 200 - num_children

    # Calculate the number of female adults present
    num_female_adults = num_adults - num_male_adults
    result = num_female_adults
    return result

print(solution())