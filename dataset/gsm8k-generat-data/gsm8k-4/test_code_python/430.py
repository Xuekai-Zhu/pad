def solution():
    """Tanya went to the grocery store to buy some fruit.  She bought 6 pears, 4 Granny Smith apples, 2 pineapples, and a small basket of plums, which were all placed in a single paper bag.  Unfortunately, the bag that the fruit had been placed in had developed a hole.  Therefore, as Tanya walked home, half of the fruit fell out of the bag.  When she later counted the fruit left in the bag, there were only 9 pieces remaining.  How many plums did she buy?"""
    # Define the initial number of fruits bought
    initial_fruits = 6 + 4 + 2 + "x" # Let x be the number of plums

    # Calculate the number of fruits that fell out of the bag
    lost_fruits = initial_fruits / 2

    # Calculate the number of fruits that remained in the bag
    remaining_fruits = 9

    # Calculate the number of plums
    plums = remaining_fruits - (6 + 4 + 2)

    # Return the result
    result = plums
    return result

print(solution())