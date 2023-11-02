def solution():
    initial_cds = 21  # Tyler starts with 21 CDs
    given_away = initial_cds // 3  # Tyler gives away a third of his CDs
    remaining_cds = initial_cds - given_away  # Tyler has this many CDs left after giving away some
    new_cds = 8  # Tyler buys 8 new CDs at the store

    # Calculate Tyler's total number of CDs now
    total_cds = remaining_cds + new_cds
    result = total_cds
    return result

print(solution())