def solution():
    """Megan went to the store and bought a dozen eggs. When she got home, her neighbor gave her another dozen eggs from her chickens. Megan used 2 eggs to make an omelet for dinner and 4 eggs to bake a cake. When Megan's aunt came over for a visit, Megan gave her half of her remaining eggs. How many eggs per meal would Megan have if she plans to divide what she has left equally for her next 3 meals?"""
    # Define the initial number of eggs
    initial_eggs = 24

    # Subtract the number of eggs used for omelet and cake
    remaining_eggs = initial_eggs - 2 - 4

    # Give half to her aunt
    aunt_eggs = remaining_eggs / 2
    remaining_eggs -= aunt_eggs

    # Divide what's left equally for 3 meals
    eggs_per_meal = remaining_eggs / 3

    result = eggs_per_meal
    return result

print(solution())