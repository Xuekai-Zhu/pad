def solution():
    """Barbi lost 1.5 kilograms each month for a year. Luca lost 9 kilograms every year for 11 years. How many more kilograms did Luca lose than Barbi?"""
    # Calculate the total weight lost by Barbi in a year
    barbi_total = 1.5 * 12

    # Calculate the total weight lost by Luca in 11 years
    luca_total = 9 * 11

    # Calculate the difference in weight lost between Luca and Barbi
    difference = luca_total - barbi_total

    # Display the difference in weight lost
    result = difference
    return result

print(solution())