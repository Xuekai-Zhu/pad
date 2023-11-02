def solution():
    """Sab and Dane sold 6 pairs of shoes that cost $3 each and 18 shirts that cost $2. How much will each of them earn if they divided their total earning?"""
    shoes_cost = 3
    pairs_sold = 6
    total_shoes_earning = shoes_cost * pairs_sold
    shirt_cost = 2
    shirts_sold = 18
    total_shirts_earning = shirt_cost * shirts_sold
    total_earning = total_shoes_earning + total_shirts_earning
    sab_earnings = total_earning / 2
    dane_earnings = total_earning / 2
    result = (sab_earnings, dane_earnings)
    return result

print(solution())