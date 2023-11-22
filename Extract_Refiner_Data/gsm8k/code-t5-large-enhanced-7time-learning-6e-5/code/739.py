def solution():
    
    # Define the number of slices on the plate initially
    initial_slices = 2

    # Define the number of slices added to the plate
    added_slices = 3

    # Define the number of slices eaten by Mara
    eaten_slices = 2

    # Define the number of slices stolen by her friend
    stolen_slices = 5

    # Calculate the total number of slices on the plate
    total_slices = initial_slices + added_slices - eaten_slices - stolen_slices

    # Display the total number of slices
    result = total_slices
    return result

print(solution())