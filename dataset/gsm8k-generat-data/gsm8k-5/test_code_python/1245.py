def solution():
    dozens_of_watermelons = 10  # Alice had 10 dozens of watermelons
    sold_yesterday = 0.4 * dozens_of_watermelons * 12  # Alice sold 40% yesterday (converted to individual watermelons)
    remaining_today = (1 - 0.4) * dozens_of_watermelons * 12  # Alice has the remaining watermelons today (converted to individual watermelons)
    sold_today = 0.25 * remaining_today  # Alice sold 1/4 of the remaining watermelons today
    remaining_tomorrow = remaining_today - sold_today  # Alice has the remaining watermelons tomorrow

    # Convert the remaining watermelons to dozens
    dozens_remaining = remaining_tomorrow / 12
    result = dozens_remaining
    return result

print(solution())