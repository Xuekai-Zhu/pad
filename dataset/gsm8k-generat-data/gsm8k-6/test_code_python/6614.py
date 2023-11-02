def solution():
    # Calculate the total number of baby snakes
    baby_snakes = 3 * 2  # each snake lays 2 eggs

    # Calculate the total amount of money from selling the baby snakes
    normal_baby_snakes = baby_snakes - 1  # all but one baby snake sell for $250
    rare_baby_snake = 1  # one baby snake is super rare and sells for 4 times as much
    total_money = (normal_baby_snakes * 250) + (rare_baby_snake * 1000)
    result = total_money
    return result

print(solution())