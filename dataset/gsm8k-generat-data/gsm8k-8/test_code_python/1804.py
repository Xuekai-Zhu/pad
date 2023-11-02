def solution():
    # Define the number of dice each person brought
    tom_dice = 4
    tim_dice = 4

    # Define the number of sides on each die
    sides_per_die = 6

    # Calculate the total number of sides
    total_sides = (tom_dice + tim_dice) * sides_per_die
    result = total_sides
    return result

print(solution())