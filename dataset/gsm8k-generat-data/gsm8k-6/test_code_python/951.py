def solution():
    # Calculate the total number of people attending Michonne's party
    school_friends = 6
    neighborhood_friends = 12
    extra_friends = (6 + 12) * 2  # each friend brings 2 extra friends along
    total_people = school_friends + neighborhood_friends + extra_friends
    result = total_people
    return result

print(solution())