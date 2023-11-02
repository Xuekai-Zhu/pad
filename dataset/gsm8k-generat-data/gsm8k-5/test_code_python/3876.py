def solution():
    thursday_sales = 210  # Meat Market sold 210kg of ground beef on Thursday
    friday_sales = 2 * thursday_sales  # Meat Market sold twice as much on Friday
    saturday_sales = 130  # Meat Market sold 130kg on Saturday
    sunday_sales = saturday_sales / 2  # Meat Market sold half of what they sold on Saturday on Sunday

    total_sales = thursday_sales + friday_sales + saturday_sales + sunday_sales
    excess_sales = total_sales - 500  # Excess sales beyond their original plans

    result = excess_sales
    return result

print(solution())