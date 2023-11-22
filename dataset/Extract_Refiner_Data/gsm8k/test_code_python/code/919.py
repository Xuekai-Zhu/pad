def solution():
    
    # Define the total number of cups and the number of rows
    total_cups = 27
    num_rows = 3

    # Calculate the number of cups in each row
    cups_per_row = total_cups / num_rows

    # Calculate the number of cups of mint tea in each row
    mint_cups_per_row = cups_per_row - 15

    # Display the number of cups of mint tea in each row
    result = mint_cups_per_row
    return result

print(solution())