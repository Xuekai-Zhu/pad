def solution():
    sets_per_show = 5  # Carter goes through 5 sets of drum sticks per show
    sets_given_away = 6  # Carter gives away 6 new sets of drum sticks after each show
    shows_per_night = 1  # Carter plays one show per night
    nights = 30  # Carter plays for 30 nights

    # Calculate the total number of drum stick sets used by Carter
    total_sets_used = sets_per_show * shows_per_night * nights

    # Calculate the total number of drum stick sets given away by Carter
    total_sets_given_away = sets_given_away * nights

    # Calculate the total number of drum stick sets used by Carter, including the ones given away
    total_sets = total_sets_used + total_sets_given_away
    result = total_sets
    return result

print(solution())