def solution():
    """Maria is a saleswoman at a flower shop. On the first day, she sold 30 tulips and 20 roses. The next day, she doubled the previous day's sales. On the third day, she sold only 10% of the tulips sold on the second day and 16 roses. The price of one tulip is $2 and one rose is $3. How much did Maria earn over these three days?"""
    tulips_first_day = 30
    roses_first_day = 20
    tulips_second_day = tulips_first_day * 2
    roses_second_day = roses_first_day * 2
    tulips_third_day = tulips_second_day * 0.1
    roses_third_day = 16
    total_tulips = tulips_first_day + tulips_second_day + tulips_third_day
    total_roses = roses_first_day + roses_second_day + roses_third_day
    tulip_price = 2
    rose_price = 3
    total_earned = (total_tulips * tulip_price) + (total_roses * rose_price)
    result = total_earned
    return result

print(solution())