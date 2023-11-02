def solution():
    """Brad wanted to set up a lemonade stand to earn some money. Every gallon of lemonade would yield 16 glasses. He figured it would cost him $3.50 to make every gallon of lemonade. He made 2 gallons to sell and decided he would sell each glass for $1.00 He drank 5 glasses while sitting in his stand. He sold all but 6 glasses of lemonade. How much net profit did Brad earn?"""
    cost_per_gallon = 3.5
    glasses_per_gallon = 16
    total_gallons = 2
    total_glasses = total_gallons * glasses_per_gallon
    cost_of_lemonade = total_gallons * cost_per_gallon
    sold_glasses = total_glasses - 5 - 6
    revenue = sold_glasses * 1
    profit = revenue - cost_of_lemonade
    result = profit
    return result

print(solution())