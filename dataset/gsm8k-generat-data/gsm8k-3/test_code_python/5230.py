def solution():
    """Tara's parents gave her $90 for her birthday. Not wanting to spend it, Tara put the money in a new bank account that gains 10% interest annually. If she doesn't withdraw the money at all, how much will she have after a year?"""
    # Define the initial amount and interest rate
    initial_amount = 90
    interest_rate = 0.1

    # Calculate the amount after one year
    final_amount = initial_amount * (1 + interest_rate)

    # Display the final amount
    result = final_amount
    return result

print(solution())