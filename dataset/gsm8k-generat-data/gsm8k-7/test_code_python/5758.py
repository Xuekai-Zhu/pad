def solution():
    billy_picks = 36
    george_picks = billy_picks / 3
    total_picks = billy_picks + george_picks
    total_picks += 10 + 10  # They each pick 10 more after seeing the pile
    average_picks = total_picks / 2
    result = average_picks
    return result

print(solution())