def solution():
    
    # Define the initial likelihood of getting a case of 12 sodas
    case_of_12 = 12

    # Calculate the likelihood of shaking up 3 sodas
    shakes_up_3 = 3

    # Calculate the likelihood of taking 1 unshaken soda
    unshakes_left = 1

    # Calculate the likelihood of taking 1 shaken soda
    shakes_taken = 1

    # Calculate the likelihood of taking 1 unshaken soda
    unshakes_taken = 2

    # Calculate the likelihood of getting a case of 12 sodas
    case_of_12 = case_of_12 - shakes_up_3 - unshakes_left
    shakes_taken = shakes_taken + shakes_taken
    unshakes_taken = unshakes_left + unshakes_taken
    case_of_12 = case_of_12 - shakes_taken + unshakes_taken

    # Calculate the likelihood of getting a case of 12 sodas
    likelihood_of_12 = shakes_taken

print(solution())