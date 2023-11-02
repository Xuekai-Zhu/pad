def solution():
    tulips_day1 = 30
    roses_day1 = 20
    tulips_day2 = tulips_day1 * 2
    roses_day2 = roses_day1 * 2
    tulips_day3 = tulips_day2 * 0.1
    roses_day3 = 16
    tulip_price = 2
    rose_price = 3
    total_earnings = (tulips_day1 * tulip_price) + (roses_day1 * rose_price) + \
                     (tulips_day2 * tulip_price) + (roses_day2 * rose_price) + \
                     (tulips_day3 * tulip_price) + (roses_day3 * rose_price)
    result = total_earnings
    return result

print(solution())