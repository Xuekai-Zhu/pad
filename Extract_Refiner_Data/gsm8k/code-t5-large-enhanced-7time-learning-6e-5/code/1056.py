def solution():
    
    # Define the number of slices per pizza
    SLICES_PER_PIZZA = 8

    # Define the number of pizzas shared
    NUM_PIZZAS = 4

    # Calculate the total number of slices
    total_slices = SLICES_PER_PIZZA * NUM_PIZZAS

    # Subtract the slices Becky ate
    total_slices -= 10

    # Calculate the number of slices Jake ate
    jake_slices = 10 / 3

    # Subtract the slices Jake ate
    total_slices -= jake_slices

    # Calculate the number of slices Silvia ate
    silvia_slices = jake_slices * 2

    # Calculate the total slices eaten
    total_slices += silvia_slices

    # Display the total slices eaten
    result = total_slices
    return result

print(solution())