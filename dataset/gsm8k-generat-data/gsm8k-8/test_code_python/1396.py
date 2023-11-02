def solution():
    # Calculate total milk yesterday
    yesterday_morning = 68
    yesterday_evening = 82
    yesterday_total = yesterday_morning + yesterday_evening

    # Calculate milk this morning
    this_morning = yesterday_morning - 18

    # Calculate total milk today
    today_total = this_morning + yesterday_evening

    # Calculate gallons sold
    gallons_sold = yesterday_total - today_total + 24

    # Calculate revenue
    revenue = gallons_sold * 3.5
    result = revenue
    return result

print(solution())