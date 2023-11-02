def solution():
    """Maynard's dog dug 8 holes in the lawn. Maynard filled in 75% of the hole with dirt. How many holes remain unfilled?"""
    
    # Define the number of holes initially dug
    holes_initial = 8
    
    # Calculate the number of holes filled with dirt
    holes_filled = holes_initial * 0.75
    
    # Calculate the number of unfilled holes
    holes_unfilled = holes_initial - holes_filled
    
    result = holes_unfilled
    return result

print(solution())