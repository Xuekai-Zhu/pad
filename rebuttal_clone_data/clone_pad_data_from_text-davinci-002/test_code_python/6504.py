def solution():
    cost_per_dog = 250
    number_of_dogs = 2
    litter_size = 6
    cost_per_litter = cost_per_dog * number_of_dogs
    sales_price_per_puppy = 350
    total_sales = sales_price_per_puppy * litter_size
    total_profit = total_sales - cost_per_litter
    result = total_profit
    return result

print(solution())