def solution():
    # Calculate the total number of fruits that Tanya bought
    total_fruits = 6 + 4 + 2 + x  # let x be the number of plums she bought

    # Calculate the number of fruits that fell out of the bag
    lost_fruits = total_fruits / 2

    # Calculate the number of fruits left in the bag
    remaining_fruits = 9

    # Calculate the number of plums left in the bag
    plums_left = remaining_fruits - (6 + 4 + 2)  # subtract the number of other fruits from the total remaining fruits

    # Solve for x, the number of plums she bought
    x = plums_left
    result = x
    return result

print(solution())