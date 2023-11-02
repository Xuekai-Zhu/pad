def solution():
    """Iris went to the mall to buy clothes. She bought three jackets at $10 each, two pairs of shorts at $6 each, and four pairs of pants at $12 each. How much did she spend in all?"""
    jacket_price = 10
    shorts_price = 6
    pants_price = 12

    num_jackets = 3
    num_shorts = 2
    num_pants = 4

    total_spent = (num_jackets * jacket_price) + (num_shorts * shorts_price) + (num_pants * pants_price)
    result = total_spent
    return result

print(solution())