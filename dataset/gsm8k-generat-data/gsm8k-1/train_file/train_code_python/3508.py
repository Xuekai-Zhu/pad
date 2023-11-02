def solution():
    """Scott runs 3 miles every Monday through Wednesday. Then he runs twice as far he ran on Monday every Thursday and Friday. How many miles will he run in a month with 4 weeks?"""
    miles_mon_wed = 3 * 3  # 9 miles in total
    miles_thu_fri = 2 * 3  # twice the distance of Monday's run, so 2 * 3 miles
    total_miles = (miles_mon_wed * 3) + (miles_thu_fri * 2)  # Running for 4 weeks, so 3 * 3 + 2 * 2 weeks of each
    total_miles_in_month = total_miles * 4
    result = total_miles_in_month
    return result

print(solution())