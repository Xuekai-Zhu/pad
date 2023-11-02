def solution():
    """A baker is comparing the day’s sales to his daily average. He usually sells 20 pastries and 10 loaves of bread. Today, he sells 14 pastries and 25 loaves of bread. If pastries are sold for $2 and loaves of bread are sold for $4, what is the difference, in dollars, between the baker’s daily average and total for today?"""
    # Define the regular daily sales
    REGULAR_PASTRIES_SOLD = 20
    REGULAR_BREAD_SOLD = 10
    PASTRY_PRICE = 2
    BREAD_PRICE = 4

    # Calculate the total sales for today
    pastries_sold = 14
    bread_sold = 25
    today_sales = (pastries_sold * PASTRY_PRICE) + (bread_sold * BREAD_PRICE)

    # Calculate the regular daily sales
    regular_sales = (REGULAR_PASTRIES_SOLD * PASTRY_PRICE) + (REGULAR_BREAD_SOLD * BREAD_PRICE)

    # Calculate the difference between today's sales and the regular daily sales
    diff_sales = today_sales - regular_sales

    # Display the difference in sales
    result = diff_sales
    return result

print(solution())