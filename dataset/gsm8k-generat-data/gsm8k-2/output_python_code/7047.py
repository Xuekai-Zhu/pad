def solution():
    """A band's members each earn $20 per gig. If there are 4 members and they've earned $400, how many gigs have they played?"""
    member_earnings = 20
    total_earnings = 400
    num_members = 4
    total_gigs = total_earnings / (member_earnings * num_members)
    result = total_gigs
    return result

print(solution())