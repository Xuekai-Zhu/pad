def solution():
    """On Monday, a restaurant sells forty dinners. On Tuesday, it sells 40 more dinners than it did Monday. On Wednesday, it sells half the amount of dinners it sold on Tuesday. On Thursday they changed their recipe, and then sold 3 more dinners than they did on Wednesday. How many dinners were sold in those 4 days?"""
    # Define the number of dinners sold on Monday
    monday_sales = 40

    # Calculate the number of dinners sold on Tuesday
    tuesday_sales = monday_sales + 40

    # Calculate the number of dinners sold on Wednesday
    wednesday_sales = tuesday_sales / 2

    # Calculate the number of dinners sold on Thursday
    thursday_sales = wednesday_sales + 3

    # Calculate the total number of dinners sold over the four days
    total_sales = monday_sales + tuesday_sales + wednesday_sales + thursday_sales

    # Display the total number of dinners sold
    result = total_sales
    return result

print(solution())