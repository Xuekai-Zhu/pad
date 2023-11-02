def solution():
    """Alan bought a $2000 phone online. John bought it 2% more expensive in a local store. How much did John spend on his phone?"""
    alan_price = 2000
    percent_increase = 2
    john_price = alan_price * (1 + (percent_increase / 100))
    result = john_price
    return result

print(solution())