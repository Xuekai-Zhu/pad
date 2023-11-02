def solution():
    # Calculate the amount of money Zoe needs to earn from selling candy bars
    amount_to_earn = 485 - 250  # her grandma gave her $250 toward her fees
    # Calculate the number of candy bars Zoe needs to sell to earn the money
    candy_bars_needed = amount_to_earn / 1.25  # she makes $1.25 for every candy bar she sells
    result = candy_bars_needed
    return result

print(solution())