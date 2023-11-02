def solution():
    total_community_members = 2000  # The total number of community members involved in the cleaning process
    adult_men_percentage = 0.3  # 30% of the community members are adult men
    adult_men = total_community_members * adult_men_percentage  # Calculate the number of adult men
    adult_women = 2 * adult_men  # There were twice as many adult women as adult men
    total_adults = adult_men + adult_women  # Calculate the total number of adults

    # Calculate the number of children involved in the cleaning event
    children = total_community_members - total_adults
    result = children
    return result

print(solution())