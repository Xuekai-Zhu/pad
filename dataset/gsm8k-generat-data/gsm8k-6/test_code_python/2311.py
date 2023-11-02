def solution():
    # Calculate the total amount of dog food eaten in a day
    daily_food = 3 * (1/2 * 2)  # each dog eats 1/2 of a pound of food twice a day

    # Calculate the total amount of dog food eaten in a week
    weekly_food = daily_food * 7

    # Calculate the amount of dog food left after a week
    leftover_food = 30 - weekly_food
    result = leftover_food
    return result

print(solution())