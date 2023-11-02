def solution():
    """Jimmy and Tonya both like collecting matchbooks and stamps. Tonya and Jimmy decide to trade some stamps and matchbooks. They have each decided that one stamp is worth 12 matches. Each matchbook contains 24 matches. If Tonya arrives with 13 stamps, Jimmy has 5 matchbooks, and Jimmy trades all his matchbooks for stamps, how many stamps does Tonya have left?"""
    stamps_per_match = 1/12
    matches_per_book = 24
    jimmy_matchbooks = 5
    jimmy_matches = jimmy_matchbooks * matches_per_book
    jimmy_stamps = jimmy_matches * stamps_per_match
    tonya_stamps = 13
    remaining_stamps = tonya_stamps - jimmy_stamps
    result = remaining_stamps
    return result

print(solution())