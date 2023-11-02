def solution():
    """Johnson has a sack of potatoes. He gives Gina 69 potatoes, gives Tom twice as much potatoes as he gave Gina and gives one-third of the amount of potatoes he gave Tom to Anne. How many potatoes does he have left if the sack contains 300 potatoes?"""
    # Define the initial number of potatoes in the sack
    initial_potatoes = 300

    # Calculate the number of potatoes given to Gina
    gina_potatoes = 69

    # Calculate the number of potatoes given to Tom
    tom_potatoes = gina_potatoes * 2

    # Calculate the number of potatoes given to Anne
    anne_potatoes = tom_potatoes / 3

    # Calculate the total number of potatoes given away
    total_given_away = gina_potatoes + tom_potatoes + anne_potatoes

    # Calculate the number of potatoes left in the sack
    potatoes_left = initial_potatoes - total_given_away

    # Display the number of potatoes left in the sack
    result = potatoes_left
    return result

print(solution())