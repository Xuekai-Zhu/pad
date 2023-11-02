def solution():
    """Johnson has a sack of potatoes. He gives Gina 69 potatoes, gives Tom twice as much potatoes as he gave Gina and gives one-third of the amount of potatoes he gave Tom to Anne. How many potatoes does he have left if the sack contains 300 potatoes?"""
    sack_of_potatoes = 300
    gina_potatoes = 69
    tom_potatoes = 2 * gina_potatoes
    anne_potatoes = tom_potatoes / 3
    remaining_potatoes = sack_of_potatoes - gina_potatoes - tom_potatoes - anne_potatoes
    result = remaining_potatoes
    return result

print(solution())