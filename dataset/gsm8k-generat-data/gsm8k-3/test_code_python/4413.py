def solution():
    """Billy buys a 12 pack of soda from the store.  If he has twice as many brothers as sisters, and he has 2 sisters, how many sodas can he give to each of his siblings if he wants to give out the entire 12 pack while giving each the same number?"""
    # Define the number of sisters and brothers
    sisters = 2
    brothers = 2 * sisters

    # Calculate the total number of siblings
    total_siblings = sisters + brothers

    # Calculate the number of sodas each sibling can have if Billy wants to give out the entire 12 pack
    sodas_per_sibling = 12 // total_siblings

    # Display the number of sodas each sibling can have
    result = sodas_per_sibling
    return result

print(solution())