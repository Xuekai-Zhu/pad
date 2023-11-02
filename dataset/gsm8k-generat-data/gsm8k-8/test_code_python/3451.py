def solution():
    # Define the weight of green beans
    green_beans_weight = 60

    # Calculate the weight of sugar
    sugar_weight = green_beans_weight - 10

    # Calculate the weight of rice
    rice_weight = sugar_weight - 30

    # Calculate the weight of rice and sugar after the loss
    rice_after_loss = rice_weight * (2/3)
    sugar_after_loss = sugar_weight * (4/5)

    # Calculate the total weight of remaining stock
    remaining_weight = green_beans_weight + rice_after_loss + sugar_after_loss

    result = remaining_weight
    return result

print(solution())