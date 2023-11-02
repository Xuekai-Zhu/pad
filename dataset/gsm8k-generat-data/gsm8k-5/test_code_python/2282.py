def solution():
    max_price = 130  # Marcus wants to spend no more than $130
    original_price = 120  # The original price of the shoes is $120
    discount = 0.3  # Marcus gets a 30% discount on the original price

    # Calculate the discounted price after applying the discount
    discounted_price = original_price * (1 - discount)

    # Calculate the amount of money Marcus will save by buying the discounted shoes
    savings = max_price - discounted_price
    result = savings
    return result

print(solution())