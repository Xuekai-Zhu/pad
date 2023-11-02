def solution():
    total_people = 100
    women_percent = 0.5
    men_percent = 0.35

    # Calculate the number of women
    num_women = total_people * women_percent

    # Calculate the number of men
    num_men = total_people * men_percent

    # Calculate the number of children
    num_children = total_people - num_women - num_men
    result = num_children
    return result

print(solution())