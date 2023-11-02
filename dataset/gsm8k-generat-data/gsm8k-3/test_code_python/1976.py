def solution():
    """Madison makes 30 paper boats and sets them afloat. 20% are eaten by fish and Madison shoots two of the others with flaming arrows. How many boats are left?"""
    # Define the number of paper boats made
    total_boats = 30

    # Calculate the number of boats eaten by fish
    fish_eaten = int(total_boats * 0.2)

    # Calculate the number of boats shot with flaming arrows
    arrows_shot = 2

    # Calculate the number of boats left
    boats_left = total_boats - fish_eaten - arrows_shot

    # Display the number of boats left
    result = boats_left
    return result

print(solution())