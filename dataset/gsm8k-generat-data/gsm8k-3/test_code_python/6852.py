def solution():
    """Mark has the option of getting a $300 lens with a 20% discount or a $220 lens.  How much money does he save by buying the cheaper lens?"""
    # Calculate the discounted price of the more expensive lens
    discount = 0.2
    original_price = 300
    discounted_price = original_price * (1 - discount)

    # Calculate how much Mark saves by buying the cheaper lens
    cheaper_price = 220
    savings = discounted_price - cheaper_price

    # Display how much Mark saves
    result = savings
    return result

print(solution())