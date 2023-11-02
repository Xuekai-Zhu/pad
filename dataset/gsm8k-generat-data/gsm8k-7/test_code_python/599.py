def solution():
    quarters = 4
    dimes = 3
    nickel = 1
    change = 4  # 4 cents back

    # Calculate the total value of the coins used to pay for the candy bar
    total_paid = (quarters * 25) + (dimes * 10) + (nickel * 5)

    # Calculate the cost of the candy bar
    candy_cost = total_paid - change

    # Convert the cost to cents
    candy_cost_cents = candy_cost / 100.0 * 100
    result = candy_cost_cents
    return result

print(solution())