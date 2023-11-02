def solution():
    # Calculate the total chips sold in the first two weeks
    first_two_weeks = 15 + 3 * 15

    # Calculate the chips remaining to be sold in the last two weeks
    remaining_chips = 100 - first_two_weeks

    # Divide the remaining chips equally between the last two weeks
    chips_per_week = remaining_chips / 2

    result = chips_per_week
    return result

print(solution())