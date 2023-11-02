def solution():
    
    # Define the number of slices of cheese used on each sandwich
    sandwich_slices = 2

    # Define the number of slices of cheese used per omelet
    omelet_slices = sandwich_slices + 1

    # Define the number of days in the week
    days_in_week = 3

    # Calculate the total number of slices of cheese used
    total_slices = (sandwich_slices * days_in_week) + (omelet_slices * 3) + 8

    # Display the total number of slices of cheese used
    result = total_slices
    return result

print(solution())