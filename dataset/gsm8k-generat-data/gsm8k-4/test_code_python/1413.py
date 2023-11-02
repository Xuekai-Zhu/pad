def solution():
    """Maria is a saleswoman at a flower shop. On the first day, she sold 30 tulips and 20 roses. The next day, she doubled the previous day's sales. On the third day, she sold only 10% of the tulips sold on the second day and 16 roses. The price of one tulip is $2 and one rose is $3. How much did Maria earn over these three days?"""
    # Define the prices and initial sales
    TULIP_PRICE = 2
    ROSE_PRICE = 3

    tulips_day1 = 30
    roses_day1 = 20

    # Calculations for day 2
    tulips_day2 = tulips_day1 * 2
    roses_day2 = roses_day1 * 2

    # Calculations for day 3
    tulips_day3 = int(tulips_day2 * 0.1)
    roses_day3 = 16

    # Calculate the total earnings for each day
    earnings_day1 = (tulips_day1 * TULIP_PRICE) + (roses_day1 * ROSE_PRICE)
    earnings_day2 = (tulips_day2 * TULIP_PRICE) + (roses_day2 * ROSE_PRICE)
    earnings_day3 = (tulips_day3 * TULIP_PRICE) + (roses_day3 * ROSE_PRICE)

    # Calculate the total earnings over the three days
    total_earnings = earnings_day1 + earnings_day2 + earnings_day3

    # Return the result
    result = total_earnings
    return result

print(solution())