def solution():
    
    # Define the initial number of children
    initial_children = 5

    # Calculate the number of children after the first street
    children_after_first_street = initial_children + 5

    # Calculate the number of children after the second street
    children_after_second_street = children_after_first_street + 2

    # Calculate the number of children after the third street
    children_after_third_street = children_after_second_street + 2

    # Calculate the total number of children after the last street
    total_children = children_after_second_street + children_after_third_street

    # Display the total number of children
    result = total_children
    return result

print(solution())