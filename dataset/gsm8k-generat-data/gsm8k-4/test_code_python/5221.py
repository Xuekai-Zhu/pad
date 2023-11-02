def solution():
    """The chef has 60 eggs. He puts 10 eggs in the fridge and uses the rest to make cakes. If he used 5 eggs to make one cake, how many cakes did the chef make?"""
    # Define the initial number of eggs
    initial_eggs = 60

    # Define the number of eggs put in the fridge
    fridge_eggs = 10

    # Calculate the number of eggs used to make cakes
    cake_eggs = initial_eggs - fridge_eggs

    # Calculate the number of cakes the chef made
    num_cakes = cake_eggs // 5

    # Return the result
    result = num_cakes
    return result

print(solution())