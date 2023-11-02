def solution():
    """Barbi lost 1.5 kilograms each month for a year. Luca lost 9 kilograms every year for 11 years. How many more kilograms did Luca lose than Barbi?"""
    barbi_weight_loss = 1.5 * 12
    luca_weight_loss = 9 * 11
    diff_weight_loss = luca_weight_loss - barbi_weight_loss
    result = diff_weight_loss
    return result

print(solution())