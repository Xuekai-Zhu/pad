def solution():
    # Define the number of paper boats
    num_boats = 30

    # Calculate the number of boats eaten by fish
    fish_eaten = round(num_boats * 0.2)

    # Calculate the number of boats shot with flaming arrows
    arrows_shot = 2

    # Calculate the number of boats left
    boats_left = num_boats - fish_eaten - arrows_shot
    result = boats_left
    return result

print(solution())