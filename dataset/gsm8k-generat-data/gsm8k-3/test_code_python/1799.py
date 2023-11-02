def solution():
    """Silvia wants to buy a new guitar online. The price of the guitar has a suggested retail price of $1000. Guitar Center has a special deal of 15% off but has a shipping fee of $100. Sweetwater has a 10% off deal with free shipping. How much will she save by buying from the cheaper store compared to the other store?"""
    # Define the initial price of the guitar
    initial_price = 1000

    # Calculate the price after the Guitar Center deal
    gc_discount = initial_price * 0.15
    gc_shipping_fee = 100
    gc_price = initial_price - gc_discount + gc_shipping_fee

    # Calculate the price after the Sweetwater deal
    sw_discount = initial_price * 0.1
    sw_price = initial_price - sw_discount

    # Calculate the savings by buying from Sweetwater
    savings = gc_price - sw_price

    # Display the savings
    result = savings
    return result

print(solution())