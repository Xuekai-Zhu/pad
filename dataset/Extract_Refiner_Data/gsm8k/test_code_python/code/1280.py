def solution():
    
    # Define the initial number of children
    initial_children = 5

    # Calculate the number of children after the first street
    children_after_first_street = initial_children

    # Calculate the number of children after the second street
    children_after_second_street = children_after_first_street * 2

    # Calculate the number of children after the third street
    children_after_third_street = children_after_second_street * 2

    # Calculate the total number of children after the first street
    total_children = children_after_first_street + children_after_second_street + children_after_third_street

    # Calculate the number of children left after giving up and leaving the group
    children_left = 5

    # Calculate the number of children after the group gave up and leave the group
    children_after_group = children_after_third_street - children_left

    # Display the number of children after the group gave up and leave the group
    result = children_after_group
    return result

print(solution())