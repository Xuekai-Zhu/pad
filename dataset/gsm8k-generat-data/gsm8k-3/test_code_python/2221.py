def solution():
    """Diana earned $150 in July. She earned 3 times this amount in August. In September, She earned twice the money she earned in August. How much money did Diana earn over these three months?"""
    # Define the amount earned in July
    july_earnings = 150

    # Calculate the amount earned in August
    august_earnings = july_earnings * 3

    # Calculate the amount earned in September
    september_earnings = august_earnings * 2

    # Calculate the total earnings for the three months
    total_earnings = july_earnings + august_earnings + september_earnings

    # Display the total earnings
    result = total_earnings
    return result

print(solution())