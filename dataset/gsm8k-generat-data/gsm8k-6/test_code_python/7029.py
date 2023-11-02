def solution():
    # Calculate the number of marbles Hilton has in the end
    total_marbles = 26 + 6 - 10  # Hilton found 6 marbles but lost 10 marbles
    lost_marbles = 10  # number of marbles Hilton lost
    lori_gave = 2 * lost_marbles  # Lori gave Hilton twice as many marbles as he lost
    total_marbles += lori_gave  # Hilton now has the marbles that Lori gave him
    result = total_marbles
    return result

print(solution())