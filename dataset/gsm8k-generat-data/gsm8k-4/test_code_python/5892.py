def solution():
    """The community leader of a certain town organized a cleaning day event where community members were to be involved in collecting trash inside the town. Out of 2000 community members involved in the cleaning process, 30% were adult men. If there were twice as many adult women as adult men in the event, and the rest were children, calculate the total number of children involved in the cleaning event."""
    # Define the total number of community members and the percentage of adult men
    total_members = 2000
    adult_men_percentage = 0.3

    # Calculate the number of adult men and the remaining members
    adult_men = total_members * adult_men_percentage
    remaining_members = total_members - adult_men

    # Calculate the number of adult women (twice as many as adult men)
    adult_women = 2 * adult_men

    # The rest are children
    children = remaining_members - adult_women

    # return the result
    result = children
    return result

print(solution())