def solution():
    """Janet gets paid $70 an hour for exterminator work and makes $20/pound on her ant nest sculptures. If she does 20 hours of exterminator work and sells a 5-pound sculpture and a 7-pound sculpture, how much money does she make?"""
    # Define the hourly rate and sculpture price
    HOURLY_RATE = 70
    SCULPTURE_PRICE = 20

    # Calculate Janet's earnings from exterminator work
    exterminator_earnings = HOURLY_RATE * 20

    # Calculate Janet's earnings from the ant nest sculptures
    sculpture_earnings = (5 + 7) * SCULPTURE_PRICE

    # Calculate Janet's total earnings
    total_earnings = exterminator_earnings + sculpture_earnings

    # Display Janet's total earnings
    result = total_earnings
    return result

print(solution())