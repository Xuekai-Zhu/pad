def solution():
    total_people = 14 + 11 + x  # There are 14 girls, 11 boys, and x parents at the park
    num_groups = 3  # They split into 3 playgroups
    people_per_group = 25  # Each playgroup has 25 people

    # Calculate the total number of people in the park
    total_people = num_groups * people_per_group

    # Calculate the number of parents in the park
    num_parents = total_people - 14 - 11  # Subtract the number of girls and boys

    result = num_parents
    return result

print(solution())