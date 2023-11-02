def solution():
    initial_balance = 90  # Tara's parents gave her $90
    interest_rate = 0.1  # The bank account gains 10% interest annually

    # Calculate how much Tara will have after a year
    final_balance = initial_balance + (initial_balance * interest_rate)
    result = final_balance
    return result

print(solution())