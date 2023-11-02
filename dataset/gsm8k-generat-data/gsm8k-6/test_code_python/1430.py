def solution():
    # Calculate the total number of people at the park
    total_people = 14 + 11 + 2*25*3  # 14 girls, 11 boys, and 3 playgroups of 25 people each (including children and parents)

    # Calculate the number of parents at the park
    num_parents = total_people - 14 - 11  # subtract the number of girls and boys from the total number of people
    result = num_parents
    return result

print(solution())