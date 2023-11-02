def solution():
    """Johnson has a sack of potatoes. He gives Gina 69 potatoes, gives Tom twice as much potatoes as he gave Gina and gives one-third of the amount of potatoes he gave Tom to Anne. How many potatoes does he have left if the sack contains 300 potatoes?"""
    initial_potatoes = 300
    gina_potatoes = 69
    tom_potatoes = 2 * gina_potatoes
    anne_potatoes = tom_potatoes / 3
    potatoes_left = initial_potatoes - (gina_potatoes + tom_potatoes + anne_potatoes)
    result = potatoes_left
    return result

print(solution())