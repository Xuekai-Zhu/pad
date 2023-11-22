def solution():
    
    # Define the number of adults and kids in the family
    num_adults = 2
    num_kids = 4

    # Calculate the total number of slices in the family
    total_slices = num_adults * 2 + num_kids * 2

    # Calculate the percentage of the watermelon each adult gets
    adult_percentage = (num_adults / total_slices) * 100

    # Display the percentage of the watermelon each adult gets
    result = adult_percentage
    return result

print(solution())