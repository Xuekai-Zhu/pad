def solution():
    """Oliver owns a laundry shop, and he charges $2 per kilo of laundry. Two days ago, his shop washed a total of 5 kilos of laundries. Yesterday, it washed five kilos of laundries more than the previous day. Today, it washed twice the number of kilos than yesterday. How much did he earn for three days?"""
    price_per_kilo = 2
    kilos_day1 = 5
    kilos_day2 = kilos_day1 + 5
    kilos_day3 = kilos_day2 * 2
    total_kilos = kilos_day1 + kilos_day2 + kilos_day3
    earnings = total_kilos * price_per_kilo
    result = earnings
    return result

print(solution())