def solution():
    """Marie, the confectioner, makes 12 chocolate eggs, each weighing 10 ounces. She then packs an equal number of the eggs in 4 different gift boxes. Unfortunately, she leaves one of the boxes by the kitchen window and the afternoon sun melts everything. She tosses that box out. What is the total weight, in ounces, of the remaining chocolate eggs?"""
    # Define the weight of each chocolate egg
    CHOCOLATE_EGG_WEIGHT = 10

    # Get the total number of chocolate eggs
    total_chocolate_eggs = 12

    # Calculate the number of chocolate eggs in each gift box
    eggs_per_box = total_chocolate_eggs // 4

    # Calculate the total weight of the remaining chocolate eggs
    remaining_eggs = total_chocolate_eggs - eggs_per_box
    remaining_weight = remaining_eggs * CHOCOLATE_EGG_WEIGHT

    # Display the total weight of the remaining chocolate eggs
    result = remaining_weight
    return result

print(solution())