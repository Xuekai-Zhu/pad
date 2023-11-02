def solution():
    # Calculate the total amount James invested in the bank account for the year
    invested_amount = 2000 * 52  # James invested $2000 a week for 52 weeks in a year

    # Calculate the total amount James has in his bank account after the year
    total_amount = invested_amount + 250000  # James had $250,000 in his account when the year started
    windfall = total_amount * 1.5  # the windfall is worth 50% more than what James has in his account
    total_amount_with_windfall = total_amount + windfall  # calculate the total amount with the windfall

    result = total_amount_with_windfall
    return result

print(solution())