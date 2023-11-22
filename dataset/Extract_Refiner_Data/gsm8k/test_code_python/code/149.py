def solution():
    
    # Define the initial number of french fries
    initial_fries = 14

    # Calculate the number of french fries that Dave ate
    dave_fries = initial_fries / 2

    # Calculate the number of french fries that each pigeon ate
    pigeon_fries = 3 * 3

    # Calculate the number of french fries that the raccoon ate
    raccoon_fries = (2/3) * remaining_fries

    # Calculate the final number of french fries
    final_fries = initial_fries - dave_fries - pigeon_fries - raccoon_fries

    # Display the final number of french fries
    result = final_fries
    return result

print(solution())