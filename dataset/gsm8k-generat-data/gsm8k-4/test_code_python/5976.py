def solution():
    """Venus is at the deli to get subs for a party. She needs 81 inches of sub. The shop sells 5 and 8 inch subs. If she buys two 8 inch subs, how many 5 inch subs does she need to buy?"""
    # Define the length of the 8 inch subs and the total length needed
    EIGHT_INCH_LENGTH = 8
    TOTAL_LENGTH = 81

    # Calculate the length of the two 8 inch subs already purchased
    purchased_length = EIGHT_INCH_LENGTH * 2

    # Calculate the remaining length needed
    remaining_length = TOTAL_LENGTH - purchased_length

    # Calculate the number of 5 inch subs needed to make up the remaining length
    num_5_inch_subs = remaining_length // 5

    # return the result
    result = num_5_inch_subs
    return result

print(solution())