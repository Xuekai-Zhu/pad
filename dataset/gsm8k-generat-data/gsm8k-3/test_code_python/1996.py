def solution():
    """Ali has a small flower shop. He sold 4 flowers on Monday, 8 flowers on Tuesday and on Friday, he sold double the number of flowers he sold on Monday. How many flowers does Ali sell?"""
    # Define the number of flowers sold on each day
    monday_sales = 4
    tuesday_sales = 8
    friday_sales = monday_sales * 2

    # Calculate the total number of flowers sold
    total_sales = monday_sales + tuesday_sales + friday_sales

    # Display the total number of flowers sold
    result = total_sales
    return result

print(solution())