def solution():
    num_boats = 30
    percent_eaten = 0.2
    num_shot = 2

    # Calculate the number of boats eaten by fish
    num_eaten = int(num_boats * percent_eaten)

    # Calculate the number of boats remaining
    num_remaining = num_boats - num_eaten - num_shot
    result = num_remaining
    return result

print(solution())