def solution():
    tulips_price = 2
    roses_price = 3

    day1_tulips = 30
    day1_roses = 20
    day2_tulips = day1_tulips * 2
    day2_roses = day1_roses * 2
    day3_tulips = day2_tulips * 0.1
    day3_roses = 16

    # Calculate the total earnings from tulips
    total_tulips_earnings = (day1_tulips + day2_tulips + day3_tulips) * tulips_price

    # Calculate the total earnings from roses
    total_roses_earnings = (day1_roses + day2_roses + day3_roses) * roses_price

    # Calculate the total earnings from all sales
    total_earnings = total_tulips_earnings + total_roses_earnings
    result = total_earnings
    return result

print(solution())