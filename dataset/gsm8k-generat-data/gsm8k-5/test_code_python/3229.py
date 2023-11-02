def solution():
    stanley_cups_per_hour = 4  # Stanley sells 4 cups of lemonade per hour
    carl_cups_per_hour = 7  # Carl sells 7 cups of lemonade per hour
    hours = 3  # Stanley and Carl sell lemonade for 3 hours

    # Calculate the total number of cups sold by Stanley and Carl
    stanley_cups_total = stanley_cups_per_hour * hours
    carl_cups_total = carl_cups_per_hour * hours

    # Calculate the difference in cups sold between Carl and Stanley
    cups_difference = carl_cups_total - stanley_cups_total
    result = cups_difference
    return result

print(solution())