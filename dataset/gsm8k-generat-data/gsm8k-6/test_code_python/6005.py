def solution():
    # Calculate the total number of apartments in the building
    total_apartments = 25 * 4  # 25 floors with 4 apartments on each floor
    # Calculate the total number of people living in the building
    total_people = total_apartments * 2  # each apartment houses two people
    result = total_people
    return result

print(solution())