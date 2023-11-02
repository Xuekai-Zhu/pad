def solution():
    # Calculate the number of female adults
    female_adults = 100 + 50  # 50 more female adults than male adults

    # Calculate the total number of adults
    total_adults = 100 + female_adults

    # Calculate the total number of children
    children = total_adults * 2  # twice the total number of adults

    # Calculate the total number of people who attended the family reunion
    total_attendees = total_adults + children

    result = total_attendees
    return result

print(solution())