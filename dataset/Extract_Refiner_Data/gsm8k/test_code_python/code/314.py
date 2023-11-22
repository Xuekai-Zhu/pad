def solution():
    
    # Define the number of boys
    boys = 30

    # Calculate the number of girls
    girls = boys * 3

    # Calculate the number of nongendered children
    nongendered = boys / 10

    # Calculate the total number of children
    total_children = boys + girls + nongendered

    # Display the total number of children
    result = total_children
    return result

print(solution())