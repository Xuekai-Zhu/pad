def solution():
    
    # Define the number of apples that fell out of the tree
    total_apples = 2

    # Define the number of apples that fell out of the tree after the first failure
    apples_after_first_failure = 1

    # Define the number of apples that fell out of the tree after the second failure
    apples_after_second_failure = 2

    # Define the number of apples that fell out of the tree after the third failure
    apples_after_third_failure = 6

    # Calculate the total number of apples picked up by Newton
    total_picked_up = apples_after_first_failure + apples_after_second_failure + apples_after_third_failure

    # Display the total number of apples picked up by Newton
    result = total_picked_up
    return result

print(solution())