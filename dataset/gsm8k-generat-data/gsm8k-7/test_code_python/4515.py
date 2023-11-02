def solution():
    price_per_kilo = 2
    kilos_day1 = 5
    kilos_day2 = kilos_day1 + 5
    kilos_day3 = 2 * kilos_day2

    # Calculate the total earnings for each day
    earnings_day1 = kilos_day1 * price_per_kilo
    earnings_day2 = kilos_day2 * price_per_kilo
    earnings_day3 = kilos_day3 * price_per_kilo

    # Calculate the total earnings for all three days
    total_earnings = earnings_day1 + earnings_day2 + earnings_day3
    result = total_earnings
    return result

print(solution())