def solution():
    """Angela has a collection of 24 pieces of rare action figures. She sold off a quarter of them at the pawnshop and gave one-third of the remainder to her daughter. How many does she have left?"""
    # Define the size of Angela's collection and the fractions sold and given away
    collection_size = 24
    sold_fraction = 0.25
    given_away_fraction = 1/3

    # Calculate the number sold
    num_sold = collection_size * sold_fraction

    # Calculate the number remaining
    remaining = collection_size - num_sold

    # Calculate the number given away
    num_given_away = remaining * given_away_fraction

    # Calculate the number remaining after giving some away
    remaining_after_gift = remaining - num_given_away

    # Display the number of action figures that Angela has left
    result = remaining_after_gift
    return result

print(solution())