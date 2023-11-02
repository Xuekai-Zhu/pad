def solution():
    # Define the initial number of lollipops Marlon had
    initial_lollipops = 42

    # Calculate the number of lollipops Marlon gave to Emily
    emily_lollipops = (2/3) * initial_lollipops

    # Calculate the number of lollipops Marlon kept after giving some to Emily
    marlon_kept = 4

    # Calculate the number of lollipops Marlon gave to Lou
    lou_lollipops = initial_lollipops - emily_lollipops - marlon_kept
    result = lou_lollipops
    return result

print(solution())