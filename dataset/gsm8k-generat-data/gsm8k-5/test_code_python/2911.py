def solution():
    granola_bars = 20  # Greg bought a 20-pack of granola bars
    days_per_week = 7  # There are 7 days in a week

    # Greg set aside one granola bar for each day of the week
    granola_bars -= days_per_week

    # Greg traded three of the remaining granola bars to his friend Pete for a soda
    granola_bars -= 3

    # Greg gave the rest of the granola bars to his two sisters
    sister_bars = granola_bars // 2

    result = sister_bars
    return result

print(solution())