def solution():
    """Mark has the option of getting a $300 lens with a 20% discount or a $220 lens. How much money does he save by buying the cheaper lens?"""
    lens_discounted_price = 0.8 * 300
    cheaper_lens_price = 220
    savings = lens_discounted_price - cheaper_lens_price
    result = savings
    return result

print(solution())