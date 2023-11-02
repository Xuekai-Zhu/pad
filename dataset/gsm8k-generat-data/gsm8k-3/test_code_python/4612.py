def solution():
    """Samantha bought a crate of 30 eggs for $5. If she decides to sell each egg for 20 cents, how many eggs will she have left by the time she recovers her capital from the sales?"""
    # Define the cost of the crate of eggs and the selling price of each egg
    CRATE_COST = 5
    EGG_PRICE = 0.2

    # Calculate the number of eggs in the crate
    num_eggs = 30

    # Calculate the total revenue from selling all the eggs
    total_revenue = num_eggs * EGG_PRICE

    # Calculate the number of eggs Samantha needs to sell to recover her capital
    eggs_to_sell = CRATE_COST / EGG_PRICE

    # Calculate the number of eggs she will have left after selling the necessary amount
    eggs_left = num_eggs - eggs_to_sell

    # Display the number of eggs left
    result = eggs_left
    return result

print(solution())