def solution():
    """At an auction event, the price of a TV, whose cost was $500, increased by 2/5 times its initial price. The price of a phone, which was $400, also increased by 40% from its original price. If Bethany had taken both items to the auction, calculate the total amount she received for the items after the sale at the auction."""
    tv_price = 500
    phone_price = 400
    tv_increase = 2/5 * tv_price
    tv_total_price = tv_price + tv_increase
    phone_increase = 0.4 * phone_price
    phone_total_price = phone_price + phone_increase
    total_price = tv_total_price + phone_total_price
    result = total_price
    return result

print(solution())