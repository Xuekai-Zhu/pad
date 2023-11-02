def solution():
    """Jake amasses a fortune of 80 bitcoin. He donates 20 bitcoins to charity. He then gives half of all the bitcoins to his brother.
    After that, he triples the number of bitcoins he has. Then he donates another 10 coins. How many coins does he have?"""
    # Define the initial number of bitcoins
    initial_bitcoins = 80

    # Subtract the donation to charity
    bitcoins_left = initial_bitcoins - 20

    # Give half of the remaining bitcoins to his brother
    bitcoins_to_brother = bitcoins_left / 2
    bitcoins_left -= bitcoins_to_brother

    # Triple the number of remaining bitcoins
    bitcoins_left *= 3

    # Donate another 10 coins
    bitcoins_left -= 10

    result = bitcoins_left
    return result

print(solution())