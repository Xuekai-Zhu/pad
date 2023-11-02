def solution():
    """Sab and Dane sold 6 pairs of shoes that cost $3 each and 18 shirts that cost $2. How much will each of them earn if they divided their total earning?"""
    # Define the cost and number of each item sold
    SHOE_COST = 3
    SHOE_NUM = 6
    SHIRT_COST = 2
    SHIRT_NUM = 18

    # Calculate the total earnings
    total_earnings = (SHOE_COST * SHOE_NUM) + (SHIRT_COST * SHIRT_NUM)

    # Divide the total earnings between Sab and Dane
    earnings_per_person = total_earnings / 2

    # Display each person's earnings
    result = earnings_per_person
    return result

print(solution())