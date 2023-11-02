def solution():
    num_children = 4
    shoe_price = 125
    mother_discount = 0.10
    child_discount = 0.04

    # Calculate the price of the shoes after the mother discount
    discounted_price = shoe_price * (1 - mother_discount)

    # If Mrs. Brown has 3 or more children, apply the child discount
    if num_children >= 3:
        discounted_price = discounted_price * (1 - child_discount)

    result = discounted_price
    return result

print(solution())