def solution():
    # Calculate the total number of drum stick sets used by Carter
    drum_stick_sets_used = 5 * 30  # Carter uses 5 sets of drum sticks per show and plays for 30 nights
    drum_stick_sets_given_away = 6 * 30  # After each show, he gives away 6 new drum stick sets for 30 nights
    total_drum_stick_sets_used = drum_stick_sets_used + drum_stick_sets_given_away  # total number of drum stick sets used by Carter
    result = total_drum_stick_sets_used
    return result

print(solution())