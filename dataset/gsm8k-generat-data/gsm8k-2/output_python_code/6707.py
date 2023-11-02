def solution():
    """Nelly is very pleased with the painting she bought at the auction. She tells her daughter that she outbid her rival Joe by paying $2000 more than thrice his bid. If Joe’s bid was $160,000, at how much did Nelly get the painting?"""
    joe_bid = 160000
    nelly_bid = 3 * joe_bid + 2000
    result = nelly_bid
    return result

print(solution())