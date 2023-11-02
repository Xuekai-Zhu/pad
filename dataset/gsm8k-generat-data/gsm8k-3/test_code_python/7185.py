def solution():
    """Avery has 20 chickens on his farm. Each chicken lays 6 eggs. He wants to fill up egg cartons with eggs. If each egg carton can hold a dozen (12 eggs), how many egg cartons can Avery fill?"""
    # Define the number of chickens and eggs per chicken
    NUM_CHICKENS = 20
    EGGS_PER_CHICKEN = 6

    # Calculate the total number of eggs
    total_eggs = NUM_CHICKENS * EGGS_PER_CHICKEN

    # Calculate the total number of egg cartons needed
    cartons_needed = total_eggs / 12

    # Round up to the nearest integer
    cartons_needed = math.ceil(cartons_needed)

    # Display the number of egg cartons needed
    result = cartons_needed
    return result

print(solution())