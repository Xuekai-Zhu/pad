def solution():
    """A chocolate cake needs 3 eggs per cake. Cheesecake requires 8 eggs for each cheesecake. How many more eggs are needed for 9 cheesecakes than are needed for 5 chocolate cakes?"""
    # Define the number of eggs needed for each cake type
    CHOCOLATE_EGGS = 3
    CHEESECAKE_EGGS = 8

    # Calculate the total number of eggs needed for 5 chocolate cakes
    total_chocolate_eggs = CHOCOLATE_EGGS * 5

    # Calculate the total number of eggs needed for 9 cheesecakes
    total_cheesecake_eggs = CHEESECAKE_EGGS * 9

    # Calculate the difference in eggs needed for the two cake types
    egg_difference = total_cheesecake_eggs - total_chocolate_eggs

    # Return the result
    result = egg_difference
    return result

print(solution())