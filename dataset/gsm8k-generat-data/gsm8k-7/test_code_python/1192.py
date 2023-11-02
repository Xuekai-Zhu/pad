def solution():
    total_people = 120
    men_ratio = 1/3
    women_ratio = 1/2

    # Calculate the number of men who attended the party
    num_men = total_people * men_ratio

    # Calculate the number of women who attended the party
    num_women = total_people * women_ratio

    # Calculate the number of children who attended the party
    num_children = total_people - num_men - num_women

    result = num_children
    return result

print(solution())