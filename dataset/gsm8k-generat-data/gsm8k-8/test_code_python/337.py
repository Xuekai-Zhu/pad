def solution():
    # Calculate the total number of people who took either wine or soda
    total_drinks = 26 + 22 - 17

    # Calculate the total number of people who did not take either drink
    no_drinks = total_drinks - (26 + 22 - 17)

    # Calculate the total number of people at the gathering
    total_people = total_drinks + no_drinks

    result = total_people
    return result

print(solution())