def solution():
    # Let's assume Maurice's age now is x
    # After five years, Ron's age will be 43 + 5 = 48
    # After five years, Maurice's age will be x + 5
    # We know that Ron's age after five years will be four times Maurice's age after five years
    # Therefore, we can set up the equation 48 = 4(x + 5)

    x = (48/4) - 5  # Solve for x
    result = x
    return result

print(solution())