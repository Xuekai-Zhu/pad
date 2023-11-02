def solution():
    """Merill has twice as many marbles as Elliot and the two of them together have five fewer marbles than Selma. If Selma has fifty marbles, how many marbles does Merill have?"""
    # Define the number of marbles Selma has
    selma_marbles = 50

    # Calculate the number of marbles Elliot and Merill have together
    elliot_marbles = (selma_marbles + 5) / 3
    merill_marbles = 2 * elliot_marbles

    # Display the number of marbles Merill has
    result = merill_marbles
    return result

print(solution())