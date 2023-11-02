def solution():
    """Johnny buys 15 packs of colored pencils for his class. Each pack has a red, yellow, and green pencil inside. When he gets home he notices that 3 of the packs have two extra red pencils inside. How many red colored pencils did Johnny buy?"""
    # Define the number of packs of colored pencils
    num_packs = 15

    # Define the number of each color pencil in a pack
    num_red = 1
    num_yellow = 1
    num_green = 1

    # Calculate the total number of red pencils
    total_red = num_packs * num_red
    extra_red = 3 * 2
    total_red += extra_red

    # Display the total number of red pencils
    result = total_red
    return result

print(solution())