def solution():
    

    tulips_day1 = 30
    roses_day1 = 20
    tulips_day2 = tulips_day1 * 2
    roses_day2 = roses_day1 * 2
    tulips_day3 = int(tulips_day2 * 0.1)
    roses_day3 = 16

    total_tulips = tulips_day1 + tulips_day2 + tulips_day3
    total_roses = roses_day1 + roses_day2 + roses_day3

    revenue_tulips = total_tulips * 2
    revenue_roses = total_roses * 3

    total_revenue = revenue_tulips + revenue_roses

    result = total_revenue

    return result

print(solution())