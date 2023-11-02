def solution():
    eggs_in_crate = 30  # Samantha bought a crate of 30 eggs
    cost_of_crate = 5  # Samantha spent $5 to buy the crate of eggs
    cost_per_egg = cost_of_crate / eggs_in_crate  # The cost per egg is $5/30 = $0.1667
    selling_price_per_egg = 0.20  # Samantha wants to sell each egg for 20 cents

    # Calculate how many eggs Samantha needs to sell to recover her capital
    eggs_to_sell = int(cost_of_crate / (selling_price_per_egg - cost_per_egg)) + 1

    # Calculate how many eggs will be left after Samantha recovers her capital
    eggs_left = eggs_in_crate - eggs_to_sell

    result = eggs_left
    return result

print(solution())