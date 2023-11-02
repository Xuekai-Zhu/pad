def solution():
    sticks_per_show = 5
    sticks_given_away_per_show = 6
    num_nights = 30

    # Calculate the total number of new sets of drum sticks given away
    total_given_away = sticks_given_away_per_show * num_nights

    # Calculate the total number of sets of drum sticks used by Carter
    total_used = sticks_per_show * num_nights

    # Calculate the total number of sets of drum sticks that Carter goes through
    total_sticks = total_used + total_given_away
    result = total_sticks
    return result

print(solution())