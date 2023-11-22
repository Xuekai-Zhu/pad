def solution():
    
    # Define the number of slices per pizza
    SLICES_PER_PIZZA = 12

    # Define the number of people Bryce and his friends
    num_people = 4

    # Calculate the total number of slices
    total_slices = num_people * SLICES_PER_PIZZA

    # Calculate the number of slices eaten by Bryce and his friends
    slices_eaten = (2/3) * num_slices * (num_people / 2)

    # Calculate the number of slices eaten by the two remaining friends
    slices_eaten += (2/4) * num_slices * (num_people / 2)

    # Calculate the number of slices left
    slices_left = total_slices - slices_eaten

    # Display the number of slices left
    result = slices_left
    return result

print(solution())