def solution():
    
    day1 = 5
    day2 = day1 + 5
    day3 = 2 * day2
    total_kilos = day1 + day2 + day3
    price_per_kilo = 2
    total_earnings = total_kilos * price_per_kilo
    result = total_earnings
    return result

print(solution())