def solution():
    initial_total = 59  # They initially collected 59 seashells
    henry_collected = 11  # Henry collected 11 seashells
    paul_collected = 24  # Paul collected 24 seashells
    leo_collected = initial_total - henry_collected - paul_collected  # Calculate how many seashells Leo collected

    # Calculate how many seashells Leo gave to the younger kid
    leo_gave_away = leo_collected / 4

    # Calculate how many seashells they have left after Leo gave some away
    total_left = initial_total - leo_gave_away

    result = total_left
    return result

print(solution())