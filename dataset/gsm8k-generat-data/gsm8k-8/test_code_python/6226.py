def solution():
    # Define the number of eggs in each type of omelette
    three_egg_omelette = 3
    four_egg_omelette = 4

    # Define the number of customers in each hour
    hour1_customers = 5
    hour2_customers = 7
    hour3_customers = 3
    hour4_customers = 8

    # Calculate the total number of each type of omelette ordered
    total_three_egg_omelettes = hour1_customers + hour3_customers
    total_four_egg_omelettes = hour2_customers + hour4_customers

    # Calculate the total number of eggs needed
    eggs_needed = total_three_egg_omelettes * three_egg_omelette + total_four_egg_omelettes * four_egg_omelette
    result = eggs_needed
    return result

print(solution())