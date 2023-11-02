def solution():
    """James invests $2000 a week into his bank account. He had $250,000 in his account when the year started. At the end of the year, he gets a windfall that is worth 50% more than what he has in his bank account. How much money does he have?"""
    weekly_investment = 2000
    starting_balance = 250000
    total_investment = weekly_investment * 52
    ending_balance = starting_balance + total_investment
    windfall_amount = 1.5 * ending_balance
    total_amount = ending_balance + windfall_amount
    result = total_amount
    return result

print(solution())