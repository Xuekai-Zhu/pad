def solution():
    """A band's members each earn $20 per gig. If there are 4 members and they've earned $400, how many gigs have they played?"""
    # Define the payment per gig and number of band members
    PAYMENT_PER_GIG = 20
    NUM_MEMBERS = 4

    # Calculate the total payment earned by the band
    total_payment = 400

    # Calculate the number of gigs played
    num_gigs = total_payment / (PAYMENT_PER_GIG * NUM_MEMBERS)

    # Display the number of gigs played
    result = num_gigs
    return result

print(solution())