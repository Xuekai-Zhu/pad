def solution():
    """Jimmy and Tonya both like collecting matchbooks and stamps. Tonya and Jimmy decide to trade some stamps and matchbooks. They have each decided that one stamp is worth 12 matches. Each matchbook contains 24 matches. If Tonya arrives with 13 stamps, Jimmy has 5 matchbooks, and Jimmy trades all his matchbooks for stamps, how many stamps does Tonya have left?"""
    # Define the value of one stamp in matches and the number of matches per matchbook
    STAMP_VALUE = 12
    MATCHES_PER_MATCHBOOK = 24

    # Define the initial number of stamps Tonya has and the number of matchbooks Jimmy has
    tonya_stamps = 13
    jimmy_matchbooks = 5

    # Calculate the number of matches Jimmy has and the number of stamps they are worth
    jimmy_matches = jimmy_matchbooks * MATCHES_PER_MATCHBOOK
    jimmy_stamps = jimmy_matches // STAMP_VALUE

    # Calculate the number of stamps Tonya has left after trading with Jimmy
    tonya_stamps_left = tonya_stamps - jimmy_stamps

    # Display the number of stamps Tonya has left
    result = tonya_stamps_left
    return result

print(solution())