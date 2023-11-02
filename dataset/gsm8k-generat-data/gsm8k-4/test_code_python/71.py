def solution():
    """At a flea market, Hillary sells handmade crafts for 12 dollars per craft. Today, Hillary sells 3 crafts and is given an extra 7 dollars from an appreciative customer. Later on, Hillary deposits 18 dollars from today's profits into her bank account. How many dollars is Hillary left with after making the deposit?"""
    # Define the price per craft sold by Hillary
    CRAFT_PRICE = 12

    # Define the number of crafts sold by Hillary
    crafts_sold = 3

    # Define the amount of extra money Hillary receives from an appreciative customer
    extra_money = 7

    # Calculate the total amount of money earned by Hillary
    total_sales = crafts_sold * CRAFT_PRICE + extra_money

    # Define the amount of money Hillary deposits into her bank account
    deposit = 18

    # Calculate the amount of money Hillary is left with
    leftover_money = total_sales - deposit

    result = leftover_money
    return result

print(solution())