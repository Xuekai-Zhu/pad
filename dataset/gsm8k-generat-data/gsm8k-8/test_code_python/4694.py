def solution():
    # Calculate the number of leaves shed in the first week
    leaves_shed_week1 = 2/5 * 1000
    
    # Calculate the number of leaves remaining after the first week
    leaves_remaining_week2 = 1000 - leaves_shed_week1
    
    # Calculate the number of leaves shed in the second week
    leaves_shed_week2 = 0.4 * leaves_remaining_week2
    
    # Calculate the number of leaves remaining after the second week
    leaves_remaining_week3 = leaves_remaining_week2 - leaves_shed_week2
    
    # Calculate the number of leaves shed in the third week
    leaves_shed_week3 = 3/4 * leaves_shed_week2
    
    # Calculate the total number of leaves shed by the end of the third week
    total_leaves_shed = leaves_shed_week1 + leaves_shed_week2 + leaves_shed_week3
    
    # Calculate the number of leaves remaining by the end of the third week
    leaves_remaining_week3 = 1000 - total_leaves_shed
    result = leaves_remaining_week3
    return result

print(solution())