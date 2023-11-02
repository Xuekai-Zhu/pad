def solution():
    """Anna puts three slices of ham in each sandwich. If she has 31 slices of ham, how many more slices of ham does she need to make 50 ham sandwiches?"""
    slices_per_sandwich = 3
    slices_available = 31
    sandwiches_needed = 50
    slices_needed = sandwiches_needed * slices_per_sandwich
    slices_short = slices_needed - slices_available
    result = slices_short

    return result

print(solution())