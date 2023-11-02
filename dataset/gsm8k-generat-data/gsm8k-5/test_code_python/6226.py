def solution():
    eggs_for_3_egg_omelette = 3  # Each 3 egg omelette requires 3 eggs
    eggs_for_4_egg_omelette = 4  # Each 4 egg omelette requires 4 eggs

    # Customers ordering omelettes in each hour
    customers_in_hour_1 = 5
    customers_in_hour_2 = 7
    customers_in_hour_3 = 3
    customers_in_hour_4 = 8

    # Calculate the total number of eggs required for all the omelettes
    total_eggs = (customers_in_hour_1 * eggs_for_3_egg_omelette) + (customers_in_hour_2 * eggs_for_4_egg_omelette) \
                 + (customers_in_hour_3 * eggs_for_3_egg_omelette) + (customers_in_hour_4 * eggs_for_4_egg_omelette)

    result = total_eggs
    return result

print(solution())