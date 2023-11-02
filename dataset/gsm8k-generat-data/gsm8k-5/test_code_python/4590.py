def solution():
    # Calculate the total number of pomelos shipped in the two weeks
    total_pomelos = 10 * 240 + 20 * 240

    # Convert the total number of pomelos to dozens of pomelos
    dozens_of_pomelos = total_pomelos / 12

    result = dozens_of_pomelos
    return result

print(solution())