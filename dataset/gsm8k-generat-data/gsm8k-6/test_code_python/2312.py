def solution():
    # Calculate how much Lisa's mother gave her
    mother_gave = (3/5) * 1200

    # Calculate how much Lisa's brother gave her
    brother_gave = 2 * mother_gave

    # Calculate the total amount Lisa has
    total_amount = 1200 + mother_gave + brother_gave - 400

    # Calculate the price of the gift Lisa wanted to buy
    price_of_gift = total_amount

    result = price_of_gift
    return result

print(solution())