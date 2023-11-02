def solution():
    """Tameka is selling boxes of crackers for her scout troop. On Friday, she sold 40 boxes. On Saturday, she sold 10 fewer than twice that number. And on Sunday, she sold half as many as Sunday. How many boxes did she sell over the three days?"""
    # Define the number of boxes sold on Friday
    friday_sales = 40

    # Calculate the number of boxes sold on Saturday
    saturday_sales = (2 * friday_sales) - 10

    # Calculate the number of boxes sold on Sunday
    sunday_sales = friday_sales / 2

    # Calculate the total number of boxes sold over the three days
    total_sales = friday_sales + saturday_sales + sunday_sales

    # Display the total number of boxes sold
    result = total_sales
    return result

print(solution())