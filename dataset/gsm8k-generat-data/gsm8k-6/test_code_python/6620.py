def solution():
    # Calculate the weekly earnings and savings of each employee
    weekly_earnings = 10 * 10 * 5  # $10 per hour, working 10 hours a day, five days a week
    robby_savings = (2/5) * weekly_earnings
    jaylene_savings = (3/5) * weekly_earnings
    miranda_savings = 0.5 * weekly_earnings

    # Calculate the combined savings of the three employees after four weeks
    combined_savings = 4 * (robby_savings + jaylene_savings + miranda_savings)  # four weeks of savings
    result = combined_savings
    return result

print(solution())