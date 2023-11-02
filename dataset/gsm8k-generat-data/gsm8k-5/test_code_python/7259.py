def solution():
    cups_sold_last_week = 20  # Sally sold 20 cups of lemonade last week
    increase_percentage = 30/100  # Sally sold 30% more lemonade this week

    # Calculate the total cups of lemonade sold this week
    cups_sold_this_week = cups_sold_last_week + (cups_sold_last_week * increase_percentage)

    # Calculate the total cups of lemonade sold for both weeks
    total_cups_sold = cups_sold_last_week + cups_sold_this_week
    result = total_cups_sold
    return result

print(solution())