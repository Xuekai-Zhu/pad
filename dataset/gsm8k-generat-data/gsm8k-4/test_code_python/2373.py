def solution():
    """There are 60 passengers on a bus. Children make up 25% of the bus riders. How many adults are on the bus?"""
    # Define the total number of passengers and the percentage of children
    total_passengers = 60
    children_percentage = 0.25

    # Calculate the number of children on the bus
    children = total_passengers * children_percentage

    # Calculate the number of adults on the bus
    adults = total_passengers - children

    # Round the result to the nearest integer
    result = round(adults)
    return result

print(solution())