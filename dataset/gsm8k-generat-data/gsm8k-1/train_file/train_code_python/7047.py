def solution():
    """A band's members each earn $20 per gig. If there are 4 members and they've earned $400, how many gigs have they played?"""
    members = 4
    earnings_per_member = 400 / members
    earnings_per_gig = 20
    gigs_played = earnings_per_member / earnings_per_gig
    result = gigs_played
    return result

print(solution())