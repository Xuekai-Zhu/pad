def solution():
    
    # Define the initial number of slices
    slices = 12

    # Calculate the number of slices given to Bill
    bill_slices = slices * (1/3)

    # Calculate the number of slices given to Mark
    mark_slices = slices * (1/4)

    # Calculate the total number of slices given away
    total_given_away = bill_slices + mark_slices

    # Calculate the number of slices left after Jenny eats 2
    slices_left = slices - 2

    # Display the number of slices left
    result = slices_left
    return result

print(solution())