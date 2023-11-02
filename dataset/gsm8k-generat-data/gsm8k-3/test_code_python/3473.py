def solution():
    """Tricia ordered three dozen eggs. She will use 1/4 of them for making crepes, and 2/3 of the remaining for making cupcakes. How many eggs are left to make sunny-side-up eggs for breakfast?"""
    # Define the number of eggs in a dozen
    EGGS_PER_DOZEN = 12

    # Define the total number of eggs ordered
    total_eggs = 3 * EGGS_PER_DOZEN

    # Calculate the number of eggs used for crepes
    crepe_eggs = total_eggs // 4

    # Calculate the number of eggs remaining
    remaining_eggs = total_eggs - crepe_eggs

    # Calculate the number of eggs used for cupcakes
    cupcake_eggs = (2 * remaining_eggs) // 3

    # Calculate the number of eggs left for sunny-side-up eggs
    sunny_eggs = remaining_eggs - cupcake_eggs

    # Display the number of eggs left
    result = sunny_eggs
    return result

print(solution())