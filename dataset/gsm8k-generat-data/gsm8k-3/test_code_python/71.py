def solution():
    """At a flea market, Hillary sells handmade crafts for 12 dollars per craft. Today, Hillary sells 3 crafts and is given an extra 7 dollars from an appreciative customer. Later on, Hillary deposits 18 dollars from today's profits into her bank account. How many dollars is Hillary left with after making the deposit?"""
    # Define the price per craft, the number of crafts sold, and the extra amount received
    craft_price = 12
    crafts_sold = 3
    extra_amount = 7

    # Calculate the total earnings from selling crafts
    total_earnings = craft_price * crafts_sold

    # Add the extra amount to the total earnings
    total_earnings += extra_amount

    # Subtract the deposit from the total earnings
    total_earnings -= 18

    # return the result
    result = total_earnings
    return result

print(solution())