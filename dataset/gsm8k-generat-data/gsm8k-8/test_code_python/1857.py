def solution():
    # Calculate the number of female adults
    female_adults = 100 + 50

    # Calculate the total number of adults
    total_adults = 100 + female_adults

    # Calculate the number of children
    children = 2 * total_adults

    # Calculate the total number of people
    total_people = children + total_adults
    
    result = total_people
    return result

print(solution())