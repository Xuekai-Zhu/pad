def solution():
    """Alden's family invited their relatives for a family reunion on Christmas eve. There were 50 more female adults than male adults, and children were twice the total number of adults. If there were 100 male adults, how many people attended the family reunion?"""
    # Define the number of male adults
    MALE_ADULTS = 100

    # Calculate the number of female adults
    female_adults = MALE_ADULTS + 50

    # Calculate the total number of adults
    total_adults = MALE_ADULTS + female_adults

    # Calculate the number of children
    children = total_adults * 2

    # Calculate the total number of people
    total_people = MALE_ADULTS + female_adults + children

    # Display the total number of people
    result = total_people
    return result

print(solution())