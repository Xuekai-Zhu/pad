def solution():
    """Marlon had 42 lollipops in the beginning. On his way home, he saw Emily and gave her 2/3 of his lollipops. Then, Marlon kept 4 lollipops and gave the rest to Lou. How many lollipops did Lou receive?"""
    # Define the initial number of lollipops Marlon had
    initial_lollipops = 42

    # Calculate the number of lollipops Marlon gave to Emily
    emily_lollipops = int((2/3) * initial_lollipops)

    # Calculate the number of lollipops Marlon kept
    marlon_kept_lollipops = 4

    # Calculate the number of lollipops Marlon gave to Lou
    lou_lollipops = initial_lollipops - emily_lollipops - marlon_kept_lollipops

    # Display the number of lollipops Lou received
    result = lou_lollipops
    return result

print(solution())