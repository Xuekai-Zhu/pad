def solution():
    """Jake's family wants to compare the cost of the two different amusement parks. The first amusement park has a $26 fee for each adult and a $12 fee for each child; while the second amusement park has a $14 fee for each adult and $10 for each child. If there are 2 adults and 2 children in their family, how much will they be able to save if they choose the second amusement park over the first?"""
    park_1_fee = 2 * 26 + 2 * 12
    park_2_fee = 2 * 14 + 2 * 10
    savings = park_1_fee - park_2_fee
    result = savings
    return result

print(solution())