def solution():
    """Tanya went to the grocery store to buy some fruit.  She bought 6 pears, 4 Granny Smith apples, 2 pineapples, and a small basket of plums, which were all placed in a single paper bag.  Unfortunately, the bag that the fruit had been placed in had developed a hole.  Therefore, as Tanya walked home, half of the fruit fell out of the bag.  When she later counted the fruit left in the bag, there were only 9 pieces remaining.  How many plums did she buy?"""
    # Count the number of pieces of fruit Tanya had originally
    total_fruit = 6 + 4 + 2 + 1  # adding pears, apples, pineapples and plums

    # Determine how many fruit pieces were lost on the way home
    lost_fruit = total_fruit // 2

    # Determine how many fruit pieces are left in the bag
    remaining_fruit = 9

    # Determine how many plums Tanya bought
    plums = remaining_fruit - (lost_fruit - 1)  # subtracting all the fruit except the one small basket of plums

    # Display the number of plums Tanya bought
    result = plums
    return result

print(solution())