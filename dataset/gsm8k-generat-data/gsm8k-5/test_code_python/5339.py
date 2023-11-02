def solution():
    # Option 1: buy a single 16 oz package for $7
    option1_price = 7

    # Option 2: buy one 8 oz package for $4 and use a coupon to get two 4 oz packages for $2.0 each (50% discount)
    option2_price = 4 + (2*0.5*2)  # $4 for the 8 oz package + ($2 each for two 4 oz packages * 50% discount)

    # Compare the two options and choose the lowest price
    lowest_price = min(option1_price, option2_price)
    result = lowest_price
    return result

print(solution())