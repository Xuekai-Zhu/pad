def solution():
    total_marbles = 63  # The total number of marbles we have together is 63
    brother_marbles = (total_marbles - 2) / 3  # If I give my brother 2 marbles, he will have 1/3 of the total marbles
    my_marbles = 2 * (brother_marbles + 2)  # If I give my brother 2 marbles, I will have double his number of marbles
    result = my_marbles
    return result

print(solution())