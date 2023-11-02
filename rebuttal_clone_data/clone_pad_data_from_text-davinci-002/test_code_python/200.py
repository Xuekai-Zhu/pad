def solution():
    """Sansa is a famous artist, she can draw a portrait and sell it according to its size. She sells an 8-inch portrait for $5, and a 16-inch portrait for twice the price of the 8-inch portrait. If she sells three 8-inch portraits and five 16-inch portraits per day, how many does she earns every 3 days?"""
    eight_inch_portraits = 3
    sixteen_inch_portraits = 5
    days = 3
    price_eight_inch = 5
    price_sixteen_inch = 2 * price_eight_inch
    total_portraits = eight_inch_portraits + sixteen_inch_portraits
    total_price = (eight_inch_portraits * price_eight_inch) + (sixteen_inch_portraits * price_sixteen_inch)
    total_earnings = total_price * days
    result = total_earnings
    
    return result

print(solution())