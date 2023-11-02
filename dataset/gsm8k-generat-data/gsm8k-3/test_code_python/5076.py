def solution():
    """At an auction event, the price of a TV, whose cost was $500, increased by 2/5 times its initial price. The price
    of a phone, which was $400, also increased by 40% from its original price. If Bethany had taken both items to the
    auction, calculate the total amount she received for the items after the sale at the auction."""
    # Calculate the new price of the TV after the increase
    tv_increase = 2/5 * 500
    tv_new_price = 500 + tv_increase

    # Calculate the new price of the phone after the increase
    phone_increase = 0.4 * 400
    phone_new_price = 400 + phone_increase

    # Calculate the total amount received for both items
    total_amount = tv_new_price + phone_new_price

    # Display the total amount
    result = total_amount
    return result

print(solution())