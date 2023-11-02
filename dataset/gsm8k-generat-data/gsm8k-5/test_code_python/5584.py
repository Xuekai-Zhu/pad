def solution():
    # Calculate the percentage of people voting for Marty
    percent_Marty = 100 - 45 - 8  # The remaining percentage of people not voting for Biff or undecided

    # Calculate the number of people voting for Marty
    total_people = 200
    people_voting_Marty = (percent_Marty / 100) * total_people
    result = people_voting_Marty
    return result

print(solution())