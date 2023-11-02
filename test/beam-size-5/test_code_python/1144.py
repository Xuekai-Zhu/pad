def solution():
    
    # Define the number of dozens of eggs prepared
    dozens_prepared = 3

    # Define the number of eggs prepared
    eggs_prepared = dozens_prepared * 12

    # Calculate the number of eggs each child receives
    eggs_per_child = eggs_prepared // 4

    # Display the number of eggs each child receives
    result = eggs_per_child
    return result

print(solution())