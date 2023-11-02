def solution():
    full_container = 2000  # in ml
    portion_size = 200  # in ml

    # Calculate the total number of portions that Jasmine can pour from a full container
    num_portions = full_container // portion_size  # integer division

    result = num_portions
    return result

print(solution())