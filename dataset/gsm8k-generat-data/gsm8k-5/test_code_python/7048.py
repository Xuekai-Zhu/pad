def solution():
    # Calculate how much each member has earned
    earnings_per_member = 400 / 4  # $400 total earnings shared between 4 members

    # Calculate how many gigs each member has played
    gigs_per_member = earnings_per_member / 20  # Each gig pays $20

    # Multiply the number of gigs per member by the number of members
    total_gigs = gigs_per_member * 4
    result = total_gigs
    return result

print(solution())