def solution():
    total_posters = 50  # The store made 50 posters in total
    small_posters = (2 / 5) * total_posters  # Two-fifths of the posters are small
    medium_posters = 0.5 * total_posters  # Half of the posters are medium
    large_posters = total_posters - small_posters - medium_posters  # The rest are large posters

    result = large_posters
    return result

print(solution())