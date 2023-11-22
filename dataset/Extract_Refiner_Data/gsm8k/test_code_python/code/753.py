def solution():
    
    # Define the number of students who need size extra-small
    extra_small = 11

    # Calculate the number of students who need size small
    small = extra_small * 2

    # Calculate the number of students who need size medium
    medium = small / 2

    # Calculate the number of students who need size large
    large = medium + 6

    # Calculate the total number of shirts
    total_shirts = extra_small + small + medium + large

    # Display the total number of shirts
    result = total_shirts
    return result

print(solution())