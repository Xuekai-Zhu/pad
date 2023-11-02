def solution():
    # Calculate the total number of gigs Mark plays in 2 weeks
    gigs = 14 / 2  # he does a gig every other day for 2 weeks

    # Calculate the total time (in minutes) Mark plays for each gig
    time_per_gig = 2 * 5 + 2 * 5 * 2  # 2 songs of 5 minutes each and one song that is twice as long

    # Calculate the total time (in minutes) Mark played for all gigs
    total_time = gigs * time_per_gig
    result = total_time
    return result

print(solution())