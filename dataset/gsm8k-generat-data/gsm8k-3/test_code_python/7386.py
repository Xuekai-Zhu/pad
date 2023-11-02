def solution():
    """There are 80 passengers on the airplane where the number of men and women is equal. The rest of the passengers are children. How many children are on the airplane if there are 30 men?"""
    # Calculate the number of women on the airplane
    women = 80 / 2

    # Calculate the number of children on the airplane
    children = 80 - (30 + women)

    # Display the number of children
    result = children
    return result

print(solution())