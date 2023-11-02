def solution():
    selma_marbles = 50  # Selma has fifty marbles

    # Calculate the total number of marbles Elliot and Merill have together
    total_em_marbles = selma_marbles - 5  # The two of them together have five fewer marbles than Selma
    # Assuming x = the number of marbles Elliot has, then Merill has 2x marbles
    x = total_em_marbles / 3  # Dividing the marbles equally between Elliot and Merill
    merrill_marbles = 2 * x  # Merill has twice as many marbles as Elliot
    result = merrill_marbles
    return result

print(solution())