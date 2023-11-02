def solution():
    """On Tuesday, 12,000 ice cream cones were sold. On Wednesday, the number of ice cream cones sold was double the amount sold on Tuesday. How many ice cream cones have been sold in total?"""
    # Define the number of ice cream cones sold on Tuesday
    tuesday_sales = 12000

    # Calculate the number of ice cream cones sold on Wednesday
    wednesday_sales = tuesday_sales * 2

    # Calculate the total number of ice cream cones sold
    total_sales = tuesday_sales + wednesday_sales

    # Display the total number of ice cream cones sold
    result = total_sales
    return result

print(solution())