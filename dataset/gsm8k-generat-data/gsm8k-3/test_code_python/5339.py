def solution():
    """A woman needs to buy 16 oz of butter for a dessert recipe.  She can either buy a single 16 oz package of the store-brand butter for $7, or she can buy an 8oz package of store butter for $4 and use a coupon to get an additional two 4 oz packages that normally sell for $2.0 each at a 50% discount (which is applied to each 4oz package separately).  What is the lowest price she can pay for the 16 oz of butter she needs?"""
    
    # Calculate the cost of buying a 16 oz package of store-brand butter
    option1_cost = 7
    
    # Calculate the cost of buying an 8oz package and two 4 oz packages with the coupon
    option2_8oz_cost = 4
    option2_4oz_cost = (2*2.0)*0.5
    option2_cost = option2_8oz_cost + option2_4oz_cost*2
    
    # Determine which option is cheaper and return the cost
    result = min(option1_cost, option2_cost)
    return result

print(solution())