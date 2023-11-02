def solution():
    """The tooth fairy left Sharon $5.00 in exchange for the first tooth Sharon lost. Then, the tooth fairy gave Sharon $1.00 for each of the next three teeth Sharon lost. And for each of the last 2 teeth Sharon lost, the tooth fairy gave Sharon half the amount of money per tooth as Sharon had received for each of the previous three teeth. How much money did the tooth fairy leave Sharon, in dollars?"""
    first_tooth = 5
    next_three_teeth = 3 * 1
    fourth_tooth = 1 * 0.5
    fifth_tooth = 1 * 0.5
    money_total = first_tooth + next_three_teeth + fourth_tooth + fifth_tooth
    result = money_total
    return result

print(solution())