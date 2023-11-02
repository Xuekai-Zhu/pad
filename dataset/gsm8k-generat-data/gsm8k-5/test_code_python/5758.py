def solution():
    billy_picks = 36
    george_picks = billy_picks / 3

    # Total number of picks before picking additional 10 each
    total_picks = billy_picks + george_picks
    
    # Total number of picks after picking additional 10 each
    total_picks += 10 + 10
    
    # Average number of picks per person
    avg_picks = total_picks / 2
    result = avg_picks
    return result

print(solution())