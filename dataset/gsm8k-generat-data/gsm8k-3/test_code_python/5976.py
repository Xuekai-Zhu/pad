def solution():
    """Venus is at the deli to get subs for a party. She needs 81 inches of sub. The shop sells 5 and 8 inch subs. If she buys two 8 inch subs, how many 5 inch subs does she need to buy?"""
    # Define the length of each type of sub
    FIVE_INCH_SUB_LENGTH = 5
    EIGHT_INCH_SUB_LENGTH = 8

    # Define how much sub Venus needs
    needed_sub_length = 81

    # Define how many 8 inch subs Venus bought
    bought_eight_inch_subs = 2

    # Calculate the total length of the 8 inch subs Venus bought
    total_eight_inch_length = bought_eight_inch_subs * EIGHT_INCH_SUB_LENGTH

    # Calculate how much more sub Venus needs
    needed_sub_length -= total_eight_inch_length

    # Calculate how many 5 inch subs Venus needs to buy
    needed_five_inch_subs = needed_sub_length // FIVE_INCH_SUB_LENGTH

    # Display the number of 5 inch subs Venus needs to buy
    result = needed_five_inch_subs
    return result

print(solution())