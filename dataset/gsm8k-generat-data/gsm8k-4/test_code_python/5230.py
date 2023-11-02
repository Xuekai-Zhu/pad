def solution():
    """Tara's parents gave her $90 for her birthday. Not wanting to spend it, Tara put the money in a new bank account that gains 10% interest annually. If she doesn't withdraw the money at all, how much will she have after a year?"""
    # Define the initial amount of money and the interest rate
    INITIAL_AMOUNT = 90
    INTEREST_RATE = 0.1

    # Calculate the amount of money after a year, with interest
    final_amount = INITIAL_AMOUNT * (1 + INTEREST_RATE)

    result = final_amount
    return result

print(solution())