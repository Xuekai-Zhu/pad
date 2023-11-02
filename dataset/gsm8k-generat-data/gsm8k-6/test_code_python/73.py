def solution():
    # Calculate the total number of people that Roger needs to provide snack for
    total_people = 13 + 3 + 2  

    # Calculate the total number of pouches needed
    total_pouches = total_people // 6  # integer division to get number of packs needed
    if total_people % 6 != 0:  # if there are some remaining people who need snack
        total_pouches += 1  # add another pack

    result = total_pouches
    return result

print(solution())