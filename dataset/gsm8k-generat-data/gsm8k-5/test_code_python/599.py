def solution():
    total_paid = (4 * 25) + (3 * 10) + 5  # John paid with 4 quarters, 3 dimes, and a nickel
    change_received = 4  # John received 4 cents back in change

    # Calculate the cost of the candy bar
    candy_bar_cost = total_paid - change_received
    result = candy_bar_cost
    return result

print(solution())