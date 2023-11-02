def solution():
    """The selling price of a bicycle that had sold for $220 last year was increased by 15%. What is the new price?"""
    original_price = 220
    percent_increase = 15
    increase_amount = (percent_increase/100) * original_price
    new_price = original_price + increase_amount
    result = new_price
    return result

print(solution())