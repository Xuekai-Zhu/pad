def solution():
    """Jimmy and Tonya both like collecting matchbooks and stamps. Tonya and Jimmy decide to trade some stamps and matchbooks. They have each decided that one stamp is worth 12 matches. Each matchbook contains 24 matches. If Tonya arrives with 13 stamps, Jimmy has 5 matchbooks, and Jimmy trades all his matchbooks for stamps, how many stamps does Tonya have left?"""
    # Define the conversion rate between stamps and matches
    STAMPS_PER_MATCH = 1/12

    # Define the number of stamps and matchbooks
    tonya_stamps = 13
    jimmy_matchbooks = 5

    # Calculate the number of matches that Jimmy has and convert them to stamps
    jimmy_matches = jimmy_matchbooks * 24
    jimmy_stamps = jimmy_matches * STAMPS_PER_MATCH

    # Calculate the number of stamps that Tonya has left after the trade
    tonya_stamps_left = tonya_stamps - jimmy_stamps

    result = tonya_stamps_left
    return result

print(solution())