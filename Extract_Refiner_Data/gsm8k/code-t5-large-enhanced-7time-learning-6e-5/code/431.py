def solution():
    
    # Define the initial number of lollipops
    initial_lollipops = 25

    # Define the number of lollipops kept by Ray
    lollipops_kept = 5

    # Calculate the number of lollipops remaining
    lollipops_remaining = initial_lollipops - lollipops_kept

    # Calculate the number of lollipops each friend received
    lollipops_per_friend = lollipops_remaining / 4

    # Display the number of lollipops each friend received
    result = lollipops_per_friend
    return result

print(solution())