def solution():
    """A baker sells pastries for $5 and works 7 days a week. On Monday he sold 2. Every day the number of sales increases by 1 compared to the previous day. On average, how many pastries does he sell on each day of the week?"""
    # Define the price of each pastry and the number of days worked
    PASTRY_PRICE = 5
    DAYS_WORKED = 7

    # Define the number of pastries sold each day
    pastries_sold = [2]
    for i in range(1, DAYS_WORKED):
        pastries_sold.append(pastries_sold[i-1] + 1)

    # Calculate the total number of pastries sold in a week
    total_pastries_sold = sum(pastries_sold)

    # Calculate the average number of pastries sold per day
    avg_pastries_sold = total_pastries_sold / DAYS_WORKED

    # Display the average number of pastries sold per day
    result = avg_pastries_sold
    return result

print(solution())