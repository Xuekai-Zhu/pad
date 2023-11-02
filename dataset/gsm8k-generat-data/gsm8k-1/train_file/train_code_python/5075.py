def solution():
    """At an auction event, the price of a TV, whose cost was $500, increased by 2/5 times its initial price. 
    The price of a phone, which was $400, also increased by 40% from its original price. 
    If Bethany had taken both items to the auction, calculate the total amount she received for the items after the sale at the auction."""
    tv_cost = 500
    tv_increase = tv_cost * (2/5)
    tv_price = tv_cost + tv_increase
    
    phone_cost = 400
    phone_increase = phone_cost * 0.4
    phone_price = phone_cost + phone_increase
    
    total_amount = tv_price + phone_price
    result = total_amount
    return result

print(solution())