def solution():
    
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