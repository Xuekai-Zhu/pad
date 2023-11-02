def solution():
    """Sab and Dane sold 6 pairs of shoes that cost $3 each and 18 shirts that cost $2. How much will each of them earn if they divided their total earning?"""
    shoes_sold = 6
    shoe_price = 3
    shirts_sold = 18
    shirt_price = 2
    total_sales = (shoes_sold * shoe_price) + (shirts_sold * shirt_price)
    earnings_per_person = total_sales / 2
    result = earnings_per_person
    return result

print(solution())