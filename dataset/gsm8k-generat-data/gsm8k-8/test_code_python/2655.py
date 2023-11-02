def solution():
    # Calculate the fraction of decorations that were hung with nails
    nail_fraction = 2/3
    
    # Calculate the fraction of decorations that were NOT hung with nails
    non_nail_fraction = 1 - nail_fraction
    
    # Calculate the fraction of non-nail decorations that were hung with thumbtacks
    thumbtack_fraction = 2/5 * non_nail_fraction
    
    # Calculate the fraction of non-nail decorations that were hung with sticky strips
    sticky_strip_fraction = 1 - nail_fraction - thumbtack_fraction
    
    # Calculate the total number of decorations
    total_decorations = 15 / sticky_strip_fraction
    
    # Calculate the number of decorations hung with nails
    nail_count = nail_fraction * total_decorations
    
    result = nail_count
    return result

print(solution())