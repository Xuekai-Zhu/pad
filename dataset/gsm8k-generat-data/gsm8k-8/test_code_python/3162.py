def solution():
    total_marbles = 63

    # Let's call my brother's number of marbles "x"
    # If I give him 2, he will have x+2 marbles
    # And I will have 2x marbles
    # And my friend will have 3*(2x)=6x marbles

    # So we have the equation:
    # x+2 + 2x + 6x = total_marbles
    # Simplifying and solving for x:
    # 9x+2 = total_marbles
    # 9x = total_marbles - 2
    # x = (total_marbles - 2) / 9

    brother_marbles = (total_marbles - 2) / 9
    my_marbles = 2 * brother_marbles
    result = my_marbles
    return result

print(solution())