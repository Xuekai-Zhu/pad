def solution():
    eggs_collected_per_week = 8 * 2 * 12  # 8 dozen eggs per week on Tuesday and Thursday
    eggs_delivered_to_market = 3 * 12  # 3 dozen eggs delivered to the market
    eggs_delivered_to_mall = 5 * 12  # 5 dozen eggs delivered to the mall
    eggs_used_for_pie = 4 * 12  # 4 dozen eggs used to make a pie

    # Calculate the total number of eggs Mortdecai has left
    eggs_left = eggs_collected_per_week - eggs_delivered_to_market - eggs_delivered_to_mall - eggs_used_for_pie

    # Calculate the number of dozens of eggs Mortdecai donates to the charity
    dozens_of_eggs_donated = eggs_left // 12
    result = dozens_of_eggs_donated
    return result

print(solution())