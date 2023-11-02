def solution():
    """Hilton had a box of 26 marbles that he was playing with. He found 6 marbles while he was playing, but afterward realized that he had lost 10 marbles. Lori felt bad and gave Hilton twice as many marbles as he lost. How many marbles did Hilton have in the end?"""
    # Define the initial number of marbles
    initial_marbles = 26

    # Calculate the number of marbles after finding 6 and losing 10
    marbles = initial_marbles + 6 - 10

    # Calculate the number of marbles Hilton received from Lori
    lori_marbles = 2 * 10

    # Add the Lori's marbles to the total
    marbles += lori_marbles

    # return the result
    result = marbles
    return result

print(solution())