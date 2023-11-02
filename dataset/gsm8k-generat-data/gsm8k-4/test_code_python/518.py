def solution():
    """Merill has twice as many marbles as Elliot and the two of them together have five fewer marbles than Selma. If Selma has fifty marbles, how many marbles does Merill have?"""
    # Define Selma's number of marbles
    selma_marbles = 50

    # Calculate the total number of marbles for Merrill and Elliot combined
    merrill_and_elliot_marbles = selma_marbles - 5 / 2

    # Calculate Elliot's number of marbles
    elliot_marbles = merrill_and_elliot_marbles / 3

    # Calculate Merrill's number of marbles
    merrill_marbles = elliot_marbles * 2

    # Return Merrill's number of marbles
    result = merrill_marbles
    return result

print(solution())