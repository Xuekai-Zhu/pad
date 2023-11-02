def solution():
    # Calculate the total amount saved from January to July
    savings_Jan_July = 10 * 7

    # Calculate the total amount saved from August to November
    savings_Aug_Nov = 15 * 4

    # Calculate the amount needed to save in December to reach a total savings of $150 for the year
    savings_Dec = 150 - (savings_Jan_July + savings_Aug_Nov)

    result = savings_Dec
    return result

print(solution())