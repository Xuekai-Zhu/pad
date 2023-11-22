def solution():
    
    # Define the number of slices in the apple
    slices_in_apple = 8

    # Calculate the number of slices eaten by Doxa's sister and brother
    slices_sister = 1 + 1
    slices_brother = slices_sister + 1

    # Calculate the total number of slices eaten
    total_slices = slices_in_apple + slices_sister + slices_brother

    # Display the total number of slices eaten
    result = total_slices
    return result

print(solution())