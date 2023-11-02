def solution():
    
    stamps_per_matchbook = 12
    matches_per_matchbook = 24
    jimmy_matchbook_count = 5
    tonya_stamp_count = 13
    jimmy_matchbook_value = jimmy_matchbook_count * matches_per_matchbook
    jimmy_stamps_received = jimmy_matchbook_value / stamps_per_matchbook
    tonya_stamps_left = tonya_stamp_count - jimmy_stamps_received
    result = tonya_stamps_left
    return result

print(solution())