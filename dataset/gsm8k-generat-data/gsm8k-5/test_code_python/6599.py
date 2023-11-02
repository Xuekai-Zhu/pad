def solution():
    starting_potatoes = 300  # Johnson has a sack of 300 potatoes
    gina_potatoes = 69  # Johnson gives Gina 69 potatoes
    tom_potatoes = 2 * gina_potatoes  # Johnson gives Tom twice as much as he gave Gina
    anne_potatoes = tom_potatoes / 3  # Johnson gives one-third of what he gave Tom to Anne

    # Calculate the total number of potatoes given away
    total_given_away = gina_potatoes + tom_potatoes + anne_potatoes

    # Calculate the number of potatoes left
    potatoes_left = starting_potatoes - total_given_away
    result = potatoes_left
    return result

print(solution())