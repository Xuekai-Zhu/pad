def solution():
    # Calculate the number of women
    num_women = 63 * 2  # twice the number of cannoneers is equal to the number of women, and there are 63 cannoneers

    # Calculate the number of men
    num_men = 2 * num_women

    # Calculate the total number of people
    total_people = num_women + num_men + 63  # add the number of cannoneers

    result = total_people
    return result

print(solution())