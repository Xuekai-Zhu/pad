def solution():
    # Define the initial number of bees in the colony
    initial_colony_size = 80000

    # Define the threshold number of bees - a fourth of the initial number
    threshold_colony_size = initial_colony_size // 4

    # Define the rate of bee loss per day
    bee_loss_rate = 1200

    # Define the number of days it will take until the colony size drops to the threshold level
    num_days = (initial_colony_size - threshold_colony_size) // bee_loss_rate

    result = num_days
    return result

print(solution())