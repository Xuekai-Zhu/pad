def solution():
    # Calculate John's daily earnings
    daily_earnings = 250 / 10

    # Calculate how much John needs to earn to make twice the amount he's made
    twice_amount = 250 * 2
    remaining_amount = twice_amount - 250

    # Calculate how many days John needs to work to earn the remaining amount
    days_needed = remaining_amount / daily_earnings
    result = days_needed
    return result

print(solution())