def solution():
    # Calculate the earnings from washing laundry for three days
    day1_laundry = 5  # 5 kilos of laundry on day 1
    day2_laundry = day1_laundry + 5  # 5 kilos more than day 1 on day 2
    day3_laundry = 2 * day2_laundry  # twice the amount washed on day 2 on day 3
    total_laundry = day1_laundry + day2_laundry + day3_laundry  # total laundry washed in three days
    earnings = total_laundry * 2  # $2 charge per kilo of laundry
    result = earnings
    return result

print(solution())