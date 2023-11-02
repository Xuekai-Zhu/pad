def solution():
    """On Friday, Markeesha sold 30 boxes of crackers for her scout troop's fundraiser. On Saturday, she sold twice as many as on Friday. On Sunday, she sold 15 fewer than Saturday. How many boxes did she sell over the three days?"""
    # Define the number of boxes sold on each day
    friday_sales = 30
    saturday_sales = 2 * friday_sales
    sunday_sales = saturday_sales - 15

    # Calculate the total number of boxes sold over the three days
    total_sales = friday_sales + saturday_sales + sunday_sales

    # Display the total number of boxes sold
    result = total_sales
    return result

print(solution())