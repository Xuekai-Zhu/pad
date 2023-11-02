def solution():
    """Anna puts three slices of ham in each sandwich. If she has 31 slices of ham, how many more slices of ham does she need to make 50 ham sandwiches?"""
    # Define the number of slices of ham per sandwich and the number of sandwiches to be made
    HAM_PER_SANDWICH = 3
    SANDWICHES_TO_MAKE = 50

    # Calculate the total number of slices of ham needed
    total_ham_needed = HAM_PER_SANDWICH * SANDWICHES_TO_MAKE

    # Calculate the number of additional slices of ham needed
    additional_ham_needed = total_ham_needed - 31

    # return the result
    result = additional_ham_needed
    return result

print(solution())