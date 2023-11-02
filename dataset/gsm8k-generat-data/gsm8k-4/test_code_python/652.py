def solution():
    """Tanika is selling boxes of crackers for her scout troop's fund-raiser. On Saturday, she sold 60 boxes. On Sunday, she sold 50% more than on Saturday. How many boxes did she sell, in total, over the two days?"""
    # Define the number of boxes sold on Saturday
    saturday_sales = 60

    # Calculate the number of boxes sold on Sunday
    sunday_sales = saturday_sales * 1.5

    # Calculate the total number of boxes sold
    total_sales = saturday_sales + sunday_sales

    # Return the result
    result = total_sales
    return result

print(solution())