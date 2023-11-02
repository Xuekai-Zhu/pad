def solution():
    # Calculate the total cost of the video game with sales tax
    cost_with_tax = 50 + (0.1 * 50)

    # Calculate how much Nina saves each week
    savings_per_week = 10 / 2

    # Calculate how many weeks it will take Nina to save enough for the game
    weeks_to_save = cost_with_tax / savings_per_week

    result = weeks_to_save
    return result

print(solution())