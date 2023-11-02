def solution():
    """Zayne sells bracelets for $5 each and two for $8. If he started with 30 bracelets and made $60 from selling bracelets for $5 each, how much in total did he make from selling his bracelets?"""
    # Define the price options
    single_price = 5
    bundle_price = 8

    # Define the starting number of bracelets
    starting_bracelets = 30

    # Calculate the number of single bracelets sold and the remaining bracelets
    single_bracelets_sold = 12
    remaining_bracelets = starting_bracelets - single_bracelets_sold

    # Calculate the total revenue from single bracelets sold
    single_revenue = single_bracelets_sold * single_price
    bundle_revenue = remaining_bracelets // 2 * bundle_price

    # Calculate the total revenue
    total_revenue = single_revenue + bundle_revenue

    # Display the total revenue
    result = total_revenue
    return result

print(solution())