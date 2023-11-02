def solution():
    wage_per_member = 20
    num_members = 4
    total_earnings = 400

    # Calculate the total number of gigs played
    num_gigs = total_earnings / (wage_per_member * num_members)
    result = num_gigs
    return result

print(solution())