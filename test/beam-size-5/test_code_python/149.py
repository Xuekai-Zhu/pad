def solution():
    
    # Define the initial number of french fries Dave ate
    initial_fries = 14

    # Calculate the number of french fries Dave ate after the seagull landed
    dave_fries = initial_fries / 2

    # Calculate the number of french fries remaining after the pigeons bulled down
    remaining_fries = dave_fries - 3 * 3

    # Calculate the number of raccoon fries
    raccoon_fries = remaining_fries * (2/3)

    # Calculate the final number of french fries
    final_fries = remaining_fries - raccoon_fries

    # Display the final number of french fries
    result = final_fries
    return result

print(solution())