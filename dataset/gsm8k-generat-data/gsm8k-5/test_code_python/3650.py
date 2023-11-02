def solution():
    max_price = 1000  # Martin decided to spend no more than $1,000
    discount = 0.2  # The sales clerk offered an additional 20% discount
    tv_price = max_price - 100  # The sales clerk offered $100 less than the TV price

    # Calculate the discounted price of the television
    discounted_price = tv_price * (1 - discount)

    # Calculate how much lower the discounted price is than the maximum price Martin decided to spend
    lower_price = max_price - discounted_price
    result = lower_price
    return result

print(solution())