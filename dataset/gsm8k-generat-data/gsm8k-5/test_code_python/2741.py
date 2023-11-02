def solution():
    total_cost = 485  # The total cost of the field trip is $485
    grandma_money = 250  # Zoe's grandma gave her $250 towards the trip
    remaining_cost = total_cost - grandma_money  # Zoe needs to earn the remaining amount
    earnings_per_candy_bar = 1.25  # Zoe earns $1.25 for every candy bar she sells

    # Calculate the number of candy bars Zoe needs to sell
    candy_bars_needed = remaining_cost / earnings_per_candy_bar
    result = candy_bars_needed
    return result

print(solution())