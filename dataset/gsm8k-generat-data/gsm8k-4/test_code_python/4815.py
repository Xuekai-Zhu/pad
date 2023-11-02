def solution():
    """Zayne sells bracelets for $5 each and two for $8. If he started with 30 bracelets and made $60 from selling bracelets for $5 each, how much in total did he make from selling his bracelets?"""
    # Define the initial number of bracelets, the price per bracelet, and the discount price for buying two
    initial_bracelets = 30
    price_per_bracelet = 5
    discount_price = 8

    # Calculate the total revenue from selling bracelets at the regular price
    regular_revenue = 60

    # Calculate the number of bracelets sold at the regular price
    regular_bracelets = regular_revenue // price_per_bracelet

    # Calculate the number of bracelets sold at the discount price
    discount_bracelets = (initial_bracelets - regular_bracelets) // 2

    # Calculate the total revenue from selling bracelets at the discount price
    discount_revenue = discount_bracelets * discount_price

    # Calculate the total revenue from selling all of the bracelets
    total_revenue = regular_revenue + discount_revenue

    # return the result
    result = total_revenue
    return result

print(solution())