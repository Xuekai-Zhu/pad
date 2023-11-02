def solution():
    
    # Define the number of adults and kids
    num_adults = 6
    num_kids = 4

    # Calculate the total number of slices
    total_slices = num_adults * 2 + num_kids * 4

    # Calculate the percentage of watermelon each adult gets
    watermelon_percentage = (num_adults * watermelon_slices / total_slices) * 100

    # Display the percentage of watermelon each adult gets
    result = watermelon_percentage
    return result

print(solution())