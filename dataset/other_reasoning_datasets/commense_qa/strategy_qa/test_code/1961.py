def solution():
    # Define the number of children and shoes needed per child
    num_children = 8
    shoes_per_child = 2
    # Calculate the total number of shoes needed
    total_shoes_needed = num_children * shoes_per_child
    # Check if four shoes would be insufficient
    if total_shoes_needed > 4:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())