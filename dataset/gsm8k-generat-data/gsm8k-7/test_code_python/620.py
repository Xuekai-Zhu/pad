def solution():
    initial_rabbits = 13
    added_rabbits = 7

    # Calculate the total number of rabbits in the cage after the addition
    total_rabbits_in_cage = initial_rabbits + added_rabbits

    # Calculate the total number of rabbits Jasper saw in the park
    park_rabbits = total_rabbits_in_cage * 3

    result = park_rabbits
    return result

print(solution())