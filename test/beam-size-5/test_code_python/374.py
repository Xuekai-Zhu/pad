def solution():
    
    total_socks = 50
    pairs_of_socks = 10
    loose_socks = 15
    missed_socks = total_socks - (pairs_of_socks * 2) - loose_socks
    result = missed_socks
    return result

print(solution())