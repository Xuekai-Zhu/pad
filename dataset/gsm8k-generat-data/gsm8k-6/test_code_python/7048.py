def solution():
    # Calculate the number of gigs played by the band
    total_earnings = 400  # total amount earned
    earnings_per_member = 20  # each member earns $20 per gig
    num_members = 4  # number of members in the band
    num_gigs = total_earnings / (earnings_per_member * num_members)  # formula to calculate number of gigs
    result = num_gigs
    return result

print(solution())