def solution():
    """Jose owns a swimming pool. He charges $3 for kids and twice that amount for adults. If 8 kids and 10 adults swim in his swimming pool per day, how much money will he earn per week?"""
    kids_price = 3
    adults_price = 2 * kids_price
    kids_count = 8
    adults_count = 10
    daily_earnings = kids_count * kids_price + adults_count * adults_price
    weekly_earnings = daily_earnings * 7
    result = weekly_earnings
    return result

print(solution())