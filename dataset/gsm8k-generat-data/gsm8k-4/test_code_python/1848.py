def solution():
    """A floral shop had a three day sale on rose bouquets. On Monday, they sold 12 bouquets. On Tuesday, they sold three times that many bouquets. On Wednesday it rained all day and they only sold a third of what they did the day before. How many bouquets did they sell during the three day sale?"""
    # Define the number of bouquets sold on each day
    monday_sales = 12
    tuesday_sales = 3 * monday_sales
    wednesday_sales = tuesday_sales / 3

    # Calculate the total sales for the three day sale
    total_sales = monday_sales + tuesday_sales + wednesday_sales

    result = total_sales
    return result

print(solution())