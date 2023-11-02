def solution():
    """The community leader of a certain town organized a cleaning day event where community members were to be involved in collecting trash inside the town. Out of 2000 community members involved in the cleaning process, 30% were adult men. If there were twice as many adult women as adult men in the event, and the rest were children, calculate the total number of children involved in the cleaning event."""
    total_members = 2000
    adult_men_percentage = 0.3
    adult_men = total_members * adult_men_percentage
    adult_women = adult_men * 2
    children = total_members - adult_men - adult_women
    result = children
    return result

print(solution())