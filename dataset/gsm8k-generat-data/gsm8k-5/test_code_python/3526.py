def solution():
    # Calculate the cost per apple
    apple_cost = 2 / 10  # $2 for 10 apples
    # Calculate the cost per orange
    orange_cost = 1.5 / 5  # $1.50 for 5 oranges

    # Determine the cheaper fruit and calculate the cost
    if apple_cost < orange_cost:
        cheaper_fruit_cost = apple_cost * 12
    else:
        cheaper_fruit_cost = orange_cost * 12

    # Convert the cost to cents
    total_cost_cents = cheaper_fruit_cost * 100
    result = total_cost_cents
    return result

print(solution())