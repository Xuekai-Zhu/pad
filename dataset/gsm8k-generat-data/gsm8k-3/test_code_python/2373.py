def solution():
    """There are 60 passengers on a bus. Children make up 25% of the bus riders. How many adults are on the bus?"""
    # Calculate the number of children on the bus
    children = round(0.25 * 60)

    # Calculate the number of adults on the bus
    adults = 60 - children

    # Display the number of adults
    result = adults
    return result

print(solution())