def solution():
    """Jake amasses a fortune of 80 bitcoin.  He donates 20 bitcoins to charity.  He then gives half of all the bitcoins to his brother.  After that, he triples the number of bitcoins he has.  Then he donates another 10 coins.  How many coins does he have?"""
    # Define the initial number of bitcoins
    initial_bitcoins = 80

    # Donate 20 bitcoins to charity
    bitcoins = initial_bitcoins - 20

    # Give half of the remaining bitcoins to his brother
    bitcoins /= 2

    # Triple the remaining bitcoins
    bitcoins *= 3

    # Donate another 10 coins
    bitcoins -= 10

    # Display the final number of coins
    result = bitcoins
    return result

print(solution())