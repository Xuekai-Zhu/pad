def solution():
    """4 adults and 8 children are to share 8 packets of chocolate bars. Each packet contains 5 chocolate bars.
    If each adult gets 6 chocolate bars and the rest are to be shared equally among the children,
    how many will each child get?"""
    num_adults = 4
    num_children = 8
    num_packets = 8
    bars_per_packet = 5
    total_bars = num_packets * bars_per_packet
    adult_bars = num_adults * 6
    child_bars = total_bars - adult_bars
    child_share = child_bars // num_children
    result = child_share
    return result

print(solution())