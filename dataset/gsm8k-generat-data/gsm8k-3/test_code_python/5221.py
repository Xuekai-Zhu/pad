def solution():
    """The chef has 60 eggs. He puts 10 eggs in the fridge and uses the rest to make cakes. If he used 5 eggs to make one cake, how many cakes did the chef make?"""
    # Define the total number of eggs and the number in the fridge
    total_eggs = 60
    eggs_in_fridge = 10

    # Calculate the number of eggs used to make cakes
    eggs_for_cakes = total_eggs - eggs_in_fridge

    # Calculate the number of cakes
    cakes = eggs_for_cakes // 5

    # Display the number of cakes
    result = cakes
    return result

print(solution())