def solution():
    """Diana earned $150 in July. She earned 3 times this amount in August. In September, She earned twice the money she earned in August. How much money did Diana earn over these three months?"""
    # Define Diana's earnings in July
    july_earnings = 150

    # Calculate Diana's earnings in August and September
    august_earnings = july_earnings * 3
    september_earnings = august_earnings * 2

    # Calculate Diana's total earnings over the three months
    total_earnings = july_earnings + august_earnings + september_earnings

    # return the result
    result = total_earnings
    return result

print(solution())