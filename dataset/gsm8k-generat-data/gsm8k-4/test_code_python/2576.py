def solution():
    """Brad wanted to set up a lemonade stand to earn some money. Every gallon of lemonade would yield 16 glasses. He figured it would cost him $3.50 to make every gallon of lemonade. He made 2 gallons to sell and decided he would sell each glass for $1.00 He drank 5 glasses while sitting in his stand. He sold all but 6 glasses of lemonade. How much net profit did Brad earn?"""
    # Define the cost to make a gallon of lemonade
    cost_per_gallon = 3.50

    # Define the number of gallons Brad made
    gallons_made = 2

    # Calculate the total cost to make the lemonade
    total_cost = cost_per_gallon * gallons_made

    # Calculate the total number of glasses Brad made
    glasses_made = gallons_made * 16

    # Calculate the number of glasses Brad sold
    glasses_sold = glasses_made - 6

    # Calculate the total revenue Brad earned
    total_revenue = glasses_sold * 1.00

    # Calculate Brad's net profit
    net_profit = total_revenue - total_cost

    result = net_profit
    return result

print(solution())