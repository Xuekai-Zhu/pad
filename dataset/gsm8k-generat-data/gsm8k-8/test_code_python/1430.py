def solution():
    # Calculate the total number of people at the park
    total_people = 14 + 11 + 2*25*3

    # Calculate the number of parents at the park
    parents = total_people - 25*3

    result = parents
    return result

print(solution())