def solution():
    # Let's denote the number of rubber bands Bailey had by 'x'
    # Justine had 10 more rubber bands than Bailey
    justine_bands = x + 10
    # Ylona had 2 more rubber bands than Justine
    ylona_bands = justine_bands + 2
    # After giving 2 bands each to Justine and Ylona, Bailey is left with only 8 rubber bands
    x = x - 4  # Bailey gave away 4 rubber bands in total
    # Justine now has x + 2 more bands than before
    justine_bands = justine_bands + 2
    # Ylona now has x + 4 more bands than before
    ylona_bands = ylona_bands + 2
    # Thus, in the beginning, Ylona had ylona_bands rubber bands
    result = ylona_bands
    return result

print(solution())