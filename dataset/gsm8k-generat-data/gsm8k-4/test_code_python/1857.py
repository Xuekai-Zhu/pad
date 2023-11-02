def solution():
    """Alden's family invited their relatives for a family reunion on Christmas eve. There were 50 more female adults than male adults, and children were twice the total number of adults. If there were 100 male adults, how many people attended the family reunion?"""
    # Define the number of male adults and calculate the number of female adults
    male_adults = 100
    female_adults = male_adults + 50

    # Calculate the total number of adults
    total_adults = male_adults + female_adults

    # Calculate the number of children
    children = 2 * total_adults

    # Calculate the total number of people in attendance
    total_attendance = male_adults + female_adults + children

    # Return the result
    result = total_attendance
    return result

print(solution())