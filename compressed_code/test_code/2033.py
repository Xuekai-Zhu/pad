def solution():
    
    slices_per_sandwich = 3
    current_slices = 31
    sandwiches_to_make = 50
    slices_needed = sandwiches_to_make * slices_per_sandwich
    additional_slices_needed = slices_needed - current_slices
    result = additional_slices_needed
    return result

print(solution())