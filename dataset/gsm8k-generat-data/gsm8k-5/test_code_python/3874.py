def solution():
    days_per_week = 5  # Sara makes cakes during the five weekdays
    cakes_per_day = 4  # Sara makes 4 cakes per day
    selling_price = 8  # Sara sells her cakes for $8
    weeks = 4  # Sara sold all her cakes in 4 weeks

    # Calculate the total number of cakes Sara made in 4 weeks
    total_cakes = days_per_week * cakes_per_day * weeks

    # Calculate the total amount of money Sara collected by selling all her cakes
    total_money = total_cakes * selling_price
    result = total_money
    return result

print(solution())