def solution():
    """To earn money for her new computer, Tina sells handmade postcards. In a day, she can make 30 such postcards. For each postcard sold, Tina gets $5. How much money did Tina earn if she managed to sell all the postcards she made every day for 6 days?"""
    daily_postcards = 30
    selling_price = 5
    total_days = 6
    total_postcards = daily_postcards * total_days
    total_earnings = total_postcards * selling_price
    result = total_earnings
    return result

print(solution())