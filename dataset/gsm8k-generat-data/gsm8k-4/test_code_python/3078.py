def solution():
    """Barbi lost 1.5 kilograms each month for a year. Luca lost 9 kilograms every year for 11 years. How many more kilograms did Luca lose than Barbi?"""
    # Calculate the total weight lost by Barbi in one year
    barbi_weight_loss = 1.5 * 12

    # Calculate the total weight lost by Luca in 11 years
    luca_weight_loss = 9 * 11

    # Calculate the difference in weight lost between Luca and Barbi
    weight_difference = luca_weight_loss - barbi_weight_loss

    # return the result
    result = weight_difference
    return result

print(solution())