def solution():
    # Define the initial number of trays
    initial_trays = 10

    # Define the number of trays dropped
    dropped_trays = 2

    # Define the number of trays added
    added_trays = 7

    # Calculate the total number of trays for sale
    total_trays = initial_trays - dropped_trays + added_trays

    # Calculate the total number of eggs for sale
    total_eggs = total_trays * 30

    result = total_eggs
    return result

print(solution())