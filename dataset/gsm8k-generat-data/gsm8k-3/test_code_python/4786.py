def solution():
    """A chocolate cake needs 3 eggs per cake. Cheesecake requires 8 eggs for each cheesecake. How many more eggs are needed for 9 cheesecakes than are needed for 5 chocolate cakes?"""
    # Define the number of eggs needed for each type of cake
    CHOCOLATE_EGGS = 3
    CHEESECAKE_EGGS = 8

    # Define the number of each type of cake needed
    chocolate_cakes = 5
    cheesecakes = 9

    # Calculate the total number of eggs needed for the chocolate cakes
    chocolate_eggs = chocolate_cakes * CHOCOLATE_EGGS

    # Calculate the total number of eggs needed for the cheesecakes
    cheesecake_eggs = cheesecakes * CHEESECAKE_EGGS

    # Calculate the difference between the total number of eggs needed
    difference = cheesecake_eggs - chocolate_eggs

    # Display the difference in the number of eggs needed
    result = difference
    return result

print(solution())