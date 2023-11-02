def solution():
    """Chad ordered a build-your-own burrito for lunch. The base burrito is $6.50. He adds extra meat for $2.00, extra cheese for $1.00, avocado for $1.00 and 2 sauces for $0.25 each. He decides to upgrade his meal for an extra $3.00 which will add chips and a drink. He has a gift card for $5.00 that he uses at check out. How much does he still owe?"""
    base_burrito = 6.5
    extra_meat = 2
    extra_cheese = 1
    avocado = 1
    sauces = 0.25 * 2
    upgrade = 3
    gift_card = 5
    subtotal = base_burrito + extra_meat + extra_cheese + avocado + sauces
    total = subtotal + upgrade - gift_card
    result = total
    return result

print(solution())