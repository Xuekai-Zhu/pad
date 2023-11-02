def solution():
    """The community leader of a certain town organized a cleaning day event where community members were to be involved in collecting trash inside the town. Out of 2000 community members involved in the cleaning process, 30% were adult men. If there were twice as many adult women as adult men in the event, and the rest were children, calculate the total number of children involved in the cleaning event."""
    # Calculate the number of adult men involved in the cleaning process
    adult_men = 0.3 * 2000

    # Calculate the number of adult women involved in the cleaning process
    adult_women = 2 * adult_men

    # Calculate the total number of adults involved in the cleaning process
    total_adults = adult_men + adult_women

    # Calculate the number of children involved in the cleaning process
    children = 2000 - total_adults

    # Display the total number of children
    result = children
    return result

print(solution())