def solution():
    """A band's members each earn $20 per gig. If there are 4 members and they've earned $400, how many gigs have they played?"""
    # Define the number of band members and the amount they earn per gig
    num_members = 4
    earnings_per_gig = 20

    # Calculate the total amount earned by the band
    total_earnings = 400

    # Calculate the number of gigs played
    num_gigs = total_earnings / (num_members * earnings_per_gig)

    # Round the result to the nearest integer
    result = round(num_gigs)
    return result

print(solution())