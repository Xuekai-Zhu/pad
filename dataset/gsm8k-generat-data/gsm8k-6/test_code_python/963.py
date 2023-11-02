def solution():
    # Calculate the number of women at the event
    num_women = 0.5 * 40 

    # Calculate the number of children at the event before adding more
    num_children = 80 - (40 + num_women)

    # Add 10 more children to the guest list
    total_children = num_children + 10
    result = total_children
    return result

print(solution())