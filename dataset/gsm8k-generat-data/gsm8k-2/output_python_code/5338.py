def solution():
    """A woman needs to buy 16 oz of butter for a dessert recipe. She can either buy a single 16 oz package of the store-brand butter for $7, or she can buy an 8oz package of store butter for $4 and use a coupon to get an additional two 4 oz packages that normally sell for $2.0 each at a 50% discount (which is applied to each 4oz package separately). What is the lowest price she can pay for the 16 oz of butter she needs?"""
    # Option #1: Buy a single 16 oz package for $7
    option1_price = 7
    
    # Option #2: Buy an 8oz package for $4 and two 4oz packages at a discount
    option2_price = 4
    option2_price += 2 * (2 * 0.5)  # apply 50% discount to each 4oz package
    option2_price += 2  # additional $2 discount with coupon
    option2_price *= 2  # double to get 16oz

    # return the lowest price
    result = min(option1_price, option2_price)
    return result

print(solution())