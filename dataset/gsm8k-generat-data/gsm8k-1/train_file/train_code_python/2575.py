def solution():
    """Brad wanted to set up a lemonade stand to earn some money. Every gallon of lemonade would yield 16 glasses. He figured it would cost him $3.50 to make every gallon of lemonade. He made 2 gallons to sell and decided he would sell each glass for $1.00. He drank 5 glasses while sitting in his stand. He sold all but 6 glasses of lemonade. How much net profit did Brad earn?"""
    glasses_per_gallon = 16
    cost_per_gallon = 3.50
    gallons_made = 2
    glasses_made = gallons_made * glasses_per_gallon
    glasses_sold = glasses_made - 5 - 6
    revenue = glasses_sold * 1
    cost = gallons_made * cost_per_gallon
    profit = revenue - cost
    result = profit
    return result

print(solution())