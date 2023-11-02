def solution():
    """Oliver owns a laundry shop, and he charges $2 per kilo of laundry. Two days ago, his shop washed a total of 5 kilos of laundries. Yesterday, it washed five kilos of laundries more than the previous day. Today, it washed twice the number of kilos than yesterday. How much did he earn for three days?"""
    day1 = 5
    day2 = day1 + 5
    day3 = 2 * day2
    total_kilos = day1 + day2 + day3
    price_per_kilo = 2
    total_earnings = total_kilos * price_per_kilo
    result = total_earnings
    return result

print(solution())