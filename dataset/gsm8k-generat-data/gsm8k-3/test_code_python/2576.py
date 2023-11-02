def solution():
    """Brad wanted to set up a lemonade stand to earn some money.  Every gallon of lemonade would yield 16 glasses.  He figured it would cost him $3.50 to make every gallon of lemonade.  He made 2 gallons to sell and decided he would sell each glass for $1.00  He drank 5 glasses while sitting in his stand.  He sold all but 6 glasses of lemonade.  How much net profit did Brad earn?"""
    # Calculate the total cost of making the lemonade
    lemonade_cost = 2 * 3.5

    # Calculate the total number of glasses of lemonade made
    glasses_made = 2 * 16

    # Calculate the total number of glasses sold after Brad drank 5
    glasses_sold = glasses_made - 5 - 6

    # Calculate the total revenue from selling the lemonade
    revenue = glasses_sold * 1

    # Calculate the net profit
    net_profit = revenue - lemonade_cost

    # Display the net profit
    result = net_profit
    return result

print(solution())