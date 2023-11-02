def solution():
    # Define the height of the middle building
    middle_height = 100

    # Calculate the height of the building on the left
    left_height = middle_height * 0.8

    # Calculate the height of the building if left and middle were stacked
    stacked_height = middle_height + left_height

    # Calculate the height of the building on the right
    right_height = stacked_height - 20

    # Calculate the total estimated height
    total_height = left_height + middle_height + right_height
    result = total_height
    return result

print(solution())