def solution():
    # Define Brenda's weight and the given equation
    brenda_weight = 220
    brenda_equation = brenda_weight == 10 + 3 * mel_weight

    # Solve the equation for Mel's weight
    mel_weight = (brenda_weight - 10) / 3

    result = mel_weight
    return result

print(solution())