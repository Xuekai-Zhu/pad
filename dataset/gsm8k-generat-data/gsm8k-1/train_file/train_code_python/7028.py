def solution():
    """Hilton had a box of 26 marbles that he was playing with. He found 6 marbles while he was playing, but afterward realized that he had lost 10 marbles. Lori felt bad and gave Hilton twice as many marbles as he lost. How many marbles did Hilton have in the end?"""
    starting_marbles = 26
    found_marbles = 6
    lost_marbles = 10
    lori_gave = lost_marbles * 2
    total_marbles = starting_marbles + found_marbles - lost_marbles + lori_gave
    result = total_marbles
    return result

print(solution())