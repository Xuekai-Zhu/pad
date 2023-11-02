def solution():
    # Calculate the number of adult men involved in the event
    adult_men = 0.3 * 2000

    # Calculate the number of adult women involved in the event
    adult_women = 2 * adult_men

    # Calculate the number of children involved in the event
    children = 2000 - adult_men - adult_women

    result = children
    return result

print(solution())