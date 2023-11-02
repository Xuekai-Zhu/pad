def solution():
    """Milo is making a giant loaf of bread, and the recipe calls for pounds of eggs instead of telling him the number. He needs 6 pounds in total. He looks up online that an egg weighs 1/16 of a pound. If he needs 6 pounds of eggs, how many dozen should he buy?"""
    # Determine the number of eggs needed
    eggs_needed = 6 / (1/16) # 1/16 represents the weight of one egg

    # Determine the number of dozens needed
    dozens_needed = eggs_needed / 12

    # Display the number of dozens needed
    result = dozens_needed
    return result

print(solution())