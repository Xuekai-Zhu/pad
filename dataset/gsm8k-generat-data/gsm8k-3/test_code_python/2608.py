def solution():
    """Anna puts three slices of ham in each sandwich. If she has 31 slices of ham, how many more slices of ham does she need to make 50 ham sandwiches?"""
    # Define the number of slices of ham per sandwich
    HAM_PER_SANDWICH = 3

    # Get the number of slices of ham Anna has
    slices_of_ham = 31

    # Calculate the number of sandwiches Anna can make with the slices of ham she has
    sandwiches_with_ham = slices_of_ham // HAM_PER_SANDWICH

    # Calculate the number of slices of ham Anna needs to make 50 sandwiches
    slices_needed = (50 - sandwiches_with_ham) * HAM_PER_SANDWICH

    # Display the number of additional slices of ham Anna needs
    result = slices_needed
    return result

print(solution())