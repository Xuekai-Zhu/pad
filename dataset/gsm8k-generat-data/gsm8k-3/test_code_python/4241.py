def solution():
    """Three friends Wolfgang, Ludo, and Michael, went to Walmart and bought marbles. Wolfgang bought 16 marbles, Ludo bought 1/4 times more marbles than Wolfgang, and Michael bought 2/3 times as many marbles as the number of marbles both Wolfgang and Ludo bought. If they combined their marbles and decided to share them equally, how many marbles did each get?"""
    # Define the number of marbles Wolfgang bought
    wolfgang_marbles = 16

    # Calculate the number of marbles Ludo bought
    ludo_marbles = wolfgang_marbles * 1.25

    # Calculate the number of marbles both Wolfgang and Ludo bought
    wolfgang_ludo_marbles = wolfgang_marbles + ludo_marbles

    # Calculate the number of marbles Michael bought
    michael_marbles = wolfgang_ludo_marbles * (2/3)

    # Calculate the total number of marbles
    total_marbles = wolfgang_marbles + ludo_marbles + michael_marbles

    # Calculate the number of marbles each friend gets
    each_gets = total_marbles / 3

    # Display the number of marbles each friend gets
    result = each_gets
    return result

print(solution())