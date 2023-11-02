def solution():
    """Sab and Dane sold 6 pairs of shoes that cost $3 each and 18 shirts that cost $2. How much will each of them earn if they divided their total earning?"""
    # Define the prices and quantities of shoes and shirts
    shoe_price = 3
    shoe_quantity = 6
    shirt_price = 2
    shirt_quantity = 18

    # Calculate the total earnings
    total_earnings = (shoe_price * shoe_quantity) + (shirt_price * shirt_quantity)

    # Divide the total earnings equally between Sab and Dane
    earnings_per_person = total_earnings / 2

    # return the result
    result = earnings_per_person
    return result

print(solution())