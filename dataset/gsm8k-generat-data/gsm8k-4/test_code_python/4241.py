def solution():
    """Three friends Wolfgang, Ludo, and Michael, went to Walmart and bought marbles. Wolfgang bought 16 marbles, Ludo bought 1/4 times more marbles than Wolfgang, and Michael bought 2/3 times as many marbles as the number of marbles both Wolfgang and Ludo bought. If they combined their marbles and decided to share them equally, how many marbles did each get?"""
    # Define the number of marbles bought by Wolfgang
    wolfgang_marbles = 16

    # Calculate the number of marbles bought by Ludo
    ludo_marbles = wolfgang_marbles * (1 + 1/4)

    # Calculate the total number of marbles bought by Wolfgang and Ludo
    total_wolfgang_ludo_marbles = wolfgang_marbles + ludo_marbles

    # Calculate the number of marbles bought by Michael
    michael_marbles = 2 * total_wolfgang_ludo_marbles / 3

    # Calculate the total number of marbles
    total_marbles = wolfgang_marbles + ludo_marbles + michael_marbles

    # Divide the total number of marbles equally among the friends
    marbles_each = total_marbles / 3

    result = marbles_each
    return result

print(solution())