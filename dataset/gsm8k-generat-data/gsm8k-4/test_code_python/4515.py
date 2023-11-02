def solution():
    """Oliver owns a laundry shop, and he charges $2 per kilo of laundry. Two days ago, his shop washed a total of 5 kilos of laundries. Yesterday, it washed five kilos of laundries more than the previous day. Today, it washed twice the number of kilos than yesterday. How much did he earn for three days?"""
    # Define the price per kilo of laundry
    price_per_kilo = 2

    # Calculate the amount earned for the laundry washed two days ago
    laundry_day1 = 5
    laundry_day1_earnings = laundry_day1 * price_per_kilo

    # Calculate the amount earned for the laundry washed yesterday
    laundry_day2 = laundry_day1 + 5
    laundry_day2_earnings = laundry_day2 * price_per_kilo

    # Calculate the amount earned for the laundry washed today
    laundry_day3 = laundry_day2 * 2
    laundry_day3_earnings = laundry_day3 * price_per_kilo

    # Calculate the total amount earned for three days
    total_earnings = laundry_day1_earnings + laundry_day2_earnings + laundry_day3_earnings

    # return the result
    result = total_earnings
    return result

print(solution())