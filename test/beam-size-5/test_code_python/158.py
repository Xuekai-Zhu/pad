def solution():
    original_price = 20  # The original price of a bag of marbles is $20
    increase_percentage = 20  # The price increases by 20% of the original price every two months
    months = 36  # We want to know how much a bag of marbles would cost after 36 months

    # Calculate the new price after 36 months
    new_price = original_price * (1 + (increase_percentage / 100))

    result = new_price
    return result

print(solution())