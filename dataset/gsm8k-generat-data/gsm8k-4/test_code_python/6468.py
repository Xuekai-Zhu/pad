def solution():
    """Alan bought a $2000 phone online. John bought it 2% more expensive in a local store. How much did John spend on his phone?"""
    # Define the price of Alan's phone
    alan_price = 2000

    # Calculate the price of John's phone
    john_price = alan_price * 1.02

    # return the result
    result = round(john_price, 2)
    return result

print(solution())