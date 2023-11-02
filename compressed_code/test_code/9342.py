def solution():
    
    price_per_kilo = 2
    kilos_day1 = 5
    kilos_day2 = kilos_day1 + 5
    kilos_day3 = kilos_day2 * 2
    total_kilos = kilos_day1 + kilos_day2 + kilos_day3
    earnings = total_kilos * price_per_kilo
    result = earnings
    return result

print(solution())