def solution():
    """Maria is a saleswoman at a flower shop. On the first day, she sold 30 tulips and 20 roses. The next day, she doubled the previous day's sales. On the third day, she sold only 10% of the tulips sold on the second day and 16 roses. The price of one tulip is $2 and one rose is $3. How much did Maria earn over these three days?"""
    
    # Define the prices of each flower
    TULIP_PRICE = 2
    ROSE_PRICE = 3

    # Day 1 sales
    tulips1 = 30
    roses1 = 20
    day1_sales = (tulips1 * TULIP_PRICE) + (roses1 * ROSE_PRICE)

    # Day 2 sales
    tulips2 = tulips1 * 2
    roses2 = roses1 * 2
    day2_sales = (tulips2 * TULIP_PRICE) + (roses2 * ROSE_PRICE)

    # Day 3 sales
    tulips3 = int(tulips2 * 0.1)  # 10% of day 2 tulips sold
    roses3 = 16
    day3_sales = (tulips3 * TULIP_PRICE) + (roses3 * ROSE_PRICE)

    # Total earnings over 3 days
    total_sales = day1_sales + day2_sales + day3_sales

    result = total_sales
    return result

print(solution())