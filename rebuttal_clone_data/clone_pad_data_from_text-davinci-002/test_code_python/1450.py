def solution():
    pairs_of_socks = 40
    pairs_of_socks_lost = 4
    pairs_of_socks_donated = (pairs_of_socks - pairs_of_socks_lost) * (2/3)
    pairs_of_socks_purchased = 10
    pairs_of_socks_gifted = 3
    total_pairs_of_socks = pairs_of_socks_donated + pairs_of_socks_purchased + pairs_of_socks_gifted
    result = total_pairs_of_socks
    return result

print(solution())