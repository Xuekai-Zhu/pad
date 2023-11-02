def solution():
    discount_rate = 0.2
    lens_a_price = 300
    lens_b_price = 220

    # Calculate the discounted price of lens A
    lens_a_discounted_price = lens_a_price * (1 - discount_rate)

    # Determine which lens is cheaper
    cheaper_lens_price = min(lens_a_discounted_price, lens_b_price)

    # Calculate how much money is saved by buying the cheaper lens
    savings = max(lens_a_discounted_price, lens_b_price) - cheaper_lens_price
    result = savings
    return result

print(solution())