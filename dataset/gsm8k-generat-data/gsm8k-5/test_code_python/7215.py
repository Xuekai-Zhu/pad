def solution():
    pastry_average = 20  # The baker usually sells 20 pastries per day
    bread_average = 10  # The baker usually sells 10 loaves of bread per day

    pastry_sales = 14  # The baker sold 14 pastries today
    bread_sales = 25  # The baker sold 25 loaves of bread today

    pastry_revenue = pastry_sales * 2  # Pastries are sold for $2
    bread_revenue = bread_sales * 4  # Loaves of bread are sold for $4

    # Calculate the difference between the daily average and the total for today
    difference = ((pastry_average + bread_average) - (pastry_sales + bread_sales)) * ((2 + 4) / 2)
    #The (2 + 4) / 2 is to calculate the average price of a pastry and a loaf of bread

    result = difference
    return result

print(solution())