def solution():
    
    initial_cds = 21
    given_away_cds = initial_cds / 3
    remaining_cds = initial_cds - given_away_cds
    new_cds = 8
    total_cds = remaining_cds + new_cds
    result = total_cds
    return result

print(solution())