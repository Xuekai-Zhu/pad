def solution():
    """Sally sold 20 cups of lemonade last week. She sold 30% more lemonade this week. How many cups of lemonade did she sell in total for both weeks?"""
    # Define the number of cups of lemonade sold last week
    last_week_sales = 20

    # Calculate the 30% increase in sales for this week
    this_week_increase = 0.3 * last_week_sales

    # Calculate the total number of cups of lemonade sold for both weeks
    total_sales = last_week_sales + (last_week_sales * 0.3)

    # Display the total number of cups of lemonade sold for both weeks
    result = total_sales
    return result

print(solution())