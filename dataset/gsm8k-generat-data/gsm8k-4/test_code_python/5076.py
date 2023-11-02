def solution():
    """At an auction event, the price of a TV, whose cost was $500, increased by 2/5 times its initial price. 
    The price of a phone, which was $400, also increased by 40% from its original price. 
    If Bethany had taken both items to the auction, calculate the total amount she received for the items after the sale at the auction."""
    
    # Calculate the new price of the TV after the increase
    tv_price = 500 + (2/5)*500

    # Calculate the new price of the phone after the increase
    phone_price = 400 + 0.4*400

    # Calculate the total amount received for both items at the auction
    total_amount = tv_price + phone_price
    
    result = total_amount
    return result

print(solution())