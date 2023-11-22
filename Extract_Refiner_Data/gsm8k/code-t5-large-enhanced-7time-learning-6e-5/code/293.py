def solution():
    
    # Define the initial number of crates sold
    initial_sales = 120

    # Define the number of crates sold on each day
    monday_friday_sales = 20
    tuesday_sales = 15
    wednesday_sales = 12
    thursday_sales = 18

    # Calculate the total number of sales for the week
    total_sales = monday_friday_sales + tuesday_sales + wednesday_sales + thursday_sales

    # Calculate the number of crates sold for the entire week
    sold_weekend_sales = 20 + 20 + 15 + 12 + 18

    # Calculate the number of crates left from the target
    crates_off = initial_sales - total_sales

    # return the result
    result = crates_off
    return result

print(solution())