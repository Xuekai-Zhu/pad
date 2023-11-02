def solution():
    """Oliver owns a laundry shop, and he charges $2 per kilo of laundry. Two days ago, his shop washed a total of 5 kilos of laundries. Yesterday, it washed five kilos of laundries more than the previous day. Today, it washed twice the number of kilos than yesterday. How much did he earn for three days?"""
    # Define the cost per kilo of laundry
    COST_PER_KILO = 2

    # Define the number of kilos of laundry washed each day
    kilos_day1 = 5
    kilos_day2 = kilos_day1 + 5
    kilos_day3 = kilos_day2 * 2

    # Calculate the total earnings for three days
    total_earnings = (kilos_day1 + kilos_day2 + kilos_day3) * COST_PER_KILO

    # Display the total earnings
    result = total_earnings
    return result

print(solution())