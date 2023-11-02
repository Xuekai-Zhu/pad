def solution():
    """Megan went to the store and bought a dozen eggs. When she got home, her neighbor gave her another dozen eggs from her chickens. Megan used 2 eggs to make an omelet for dinner and 4 eggs to bake a cake. When Megan's aunt came over for a visit, Megan gave her half of her remaining eggs. How many eggs per meal would Megan have if she plans to divide what she has left equally for her next 3 meals?"""
    # Define the number of eggs Megan started with
    initial_eggs = 24

    # Calculate the number of eggs Megan has left after making the omelet and cake
    remaining_eggs = initial_eggs - 2 - 4

    # Calculate the number of eggs Megan's aunt took
    aunt_eggs = remaining_eggs // 2

    # Calculate the number of eggs Megan has left for her 3 meals
    meal_eggs = (remaining_eggs - aunt_eggs) // 3

    # Display the number of eggs Megan has per meal
    result = meal_eggs
    return result

print(solution())