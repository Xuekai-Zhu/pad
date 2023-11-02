def solution():
    # Find the number of people in Victoria
    people_Victoria = 3000 - 1000  # Richmond has 1000 more people than Victoria
    # Find the number of people in Beacon
    people_Beacon = people_Victoria / 4  # Victoria has 4 times as many people as Beacon
    result = people_Beacon
    return result

print(solution())