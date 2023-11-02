def solution():
    cheese_options = 3  # Denmark has 3 cheese options
    meat_options = 4  # Denmark has 4 meat options
    veg_options = 5  # Denmark has 5 vegetable options
    veg_options -= 1  # Subtract 1 as he cannot have both peppers and pepperoni

    # Calculate the total number of topping combinations
    total_combinations = cheese_options * meat_options * veg_options
    result = total_combinations
    return result

print(solution())