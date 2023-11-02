def solution():
    # Convert the number of quarters to cents
    total_quarters = 14
    total_cents = total_quarters * 25

    # Subtract half a dollar (50 cents) for candy
    total_cents -= 50

    # Return the remaining number of cents
    result = total_cents
    return result

print(solution())