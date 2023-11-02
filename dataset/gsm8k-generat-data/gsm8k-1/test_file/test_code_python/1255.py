def solution():
    """Derrick has a bakery that makes 10 dozen doughnuts every day, selling at $2 per doughnut. How much money does Derrick make in June if he sells all the doughnuts?"""
    doughnuts_per_day = 120
    price_per_doughnut = 2
    days_in_june = 30
    total_doughnuts = doughnuts_per_day * days_in_june
    total_sales = total_doughnuts * price_per_doughnut
    result = total_sales
    return result

print(solution())