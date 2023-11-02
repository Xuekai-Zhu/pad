def solution():
    """Tanya went to the grocery store to buy some fruit. She bought 6 pears, 4 Granny Smith apples, 2 pineapples, and a small basket of plums, which were all placed in a single paper bag. Unfortunately, the bag that the fruit had been placed in had developed a hole. Therefore, as Tanya walked home, half of the fruit fell out of the bag. When she later counted the fruit left in the bag, there were only 9 pieces remaining. How many plums did she buy?"""
    total_fruit = 6 + 4 + 2 + x # x is the number of plums
    remaining_fruit = total_fruit / 2

    plums_left = 9
    total_plums = x
    remaining_plums = total_plums / 2

    # We know that half of the total fruit is equal to the remaining fruit, and half of the total plums is equal to the remaining plums
    # Therefore, we can set up the following equation and solve for x:
    
    remaining_plums = total_plums / 2
    remaining_fruit = total_fruit / 2
    total_plums = x
    total_fruit = 6 + 4 + 2 + x
    remaining_plums = total_plums / 2
    remaining_fruit = total_fruit / 2
    9 = remaining_plums + remaining_fruit
    9 = (total_plums / 2) + (total_fruit / 2)
    x/2 + 6 + 4 + 2 = 9*2
    x/2 + 12 = 18
    x/2 = 6
    x = 12

    result = 12
    return result

print(solution())