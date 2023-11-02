def solution():
    """Nelly is very pleased with the painting she bought at the auction. She tells her daughter that she outbid her rival Joe by paying $2000 more than thrice his bid. If Joe’s bid was $160,000, at how much did Nelly get the painting?"""
    # Define Joe's bid and the amount Nelly outbid him by
    joe_bid = 160000
    outbid_amount = 2000

    # Calculate Nelly's bid
    nelly_bid = joe_bid * 3 + outbid_amount

    # Display the amount Nelly got the painting for
    result = nelly_bid
    return result

print(solution())