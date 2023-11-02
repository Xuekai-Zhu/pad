def solution():
    
    # Define the number of slices per pizza
    SLICES_PER_PIZZA = 8

    # Define the number of pizzas shared
    num_pizzas = 4

    # Calculate the total number of slices
    total_slices = num_pizzas * SLICES_PER_PIZZA

    # Calculate the number of slices Becky ate
    becky_slices = becky_slices + 3

    # Calculate the number of slices Jake ate
    jake_slices = becky_slices - 3

    # Calculate the number of slices Silvia ate
    silvia_slices = jake_slices * 2

    # Calculate the total number of slices eaten
    total_slices_eaten = becky_slices + jake_slices + silvia_slices

    # Display the total number of slices eaten
    result = total_slices_eaten
    return result

print(solution())