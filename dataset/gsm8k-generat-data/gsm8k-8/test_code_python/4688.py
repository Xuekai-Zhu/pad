def solution():
    # Let's call the price of the coat "c"
    # The price of the shirt is one-third of the price of the coat, so it is (1/3)c
    # The total cost of the coat and shirt is $600, so we can write an equation:
    # c + (1/3)c = $600
    # We can simplify this to:
    # (4/3)c = $600
    # To solve for the price of the coat, we can multiply both sides by 3/4:
    # c = $450
    # Now we can calculate the price of the shirt, which is (1/3)c:
    shirt_price = (1/3) * 450
    result = shirt_price
    return result

print(solution())