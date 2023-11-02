def solution():
    total_land = 20000  # Jose bought 20,000 square meters of land
    num_siblings = 4  # Jose has 4 siblings to divide the land with
    share_per_person = total_land / (num_siblings + 1)  # Jose also gets a share, so we add 1 to num_siblings

    # Calculate Jose's share
    jose_share = share_per_person

    result = jose_share
    return result

print(solution())