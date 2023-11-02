def solution():
    """Jen is planning to sell her root crops. She has 6 yams which can be sold at $1.5 each, 10 sweet potatoes that cost $2 each, and 4 carrots which cost $1.25 each. If she sells everything, how much will she earn?"""
    yam_price = 1.5
    sweet_potato_price = 2
    carrot_price = 1.25
    yams = 6
    sweet_potatoes = 10
    carrots = 4
    total_earnings = (yam_price * yams) + (sweet_potato_price * sweet_potatoes) + (carrot_price * carrots)
    result = total_earnings
    return result

print(solution())