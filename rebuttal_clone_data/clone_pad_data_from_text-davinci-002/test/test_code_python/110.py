def solution():
    
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