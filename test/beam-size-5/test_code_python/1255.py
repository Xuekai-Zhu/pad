def solution():
    doughnuts_per_dozen = 12  # There are 12 doughnuts in a dozen
    doughnuts_per_day = 10  # Derrick makes 10 dozen doughnuts every day
    price_per_doughnut = 2  # Derrick sells each doughnut for $2
    days_in_june = 30  # There are 30 days in June

    # Calculate the total number of doughnuts Derrick makes in June
    total_doughnuts = doughnuts_per_day * days_in_june

    # Calculate the total amount of money Derrick makes in June
    total_money = total_doughnuts * price_per_doughnut
    result = total_money
    return result

print(solution())