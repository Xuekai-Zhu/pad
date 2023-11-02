def solution():
    """Melanie is making meatballs for dinner. The recipe calls for breadcrumbs. To make the breadcrumbs Melanie is going to tear 2 slices of bread into smaller pieces and then add them to a blender to grind them into fine crumbs. First she tears the bread slices each in half, then tears those halves in half. How many bread pieces is Melanie going to put into the blender?"""
    
    # Define the number of slices of bread
    slices_of_bread = 2
    
    # Define the number of tears per slice
    tears_per_slice = 2
    
    # Calculate the total number of pieces of bread
    total_pieces_of_bread = slices_of_bread * tears_per_slice * tears_per_slice
    
    # Display the total number of pieces of bread
    result = total_pieces_of_bread
    return result

print(solution())