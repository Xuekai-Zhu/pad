def solution():
    """There are 80 passengers on the airplane where the number of men and women is equal. The rest of the passengers are children. How many children are on the airplane if there are 30 men?"""
    
    # Define the number of men and women on the airplane
    men = 30
    women = 30
    
    # Calculate the total number of adults on the airplane
    total_adults = men + women
    
    # Calculate the number of children on the airplane
    children = 80 - total_adults
    
    # return the result
    result = children
    return result

print(solution())