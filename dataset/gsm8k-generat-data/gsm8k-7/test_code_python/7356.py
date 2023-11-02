def solution():
    # Denmark has 3 cheese options, 4 meat options, and 5 vegetable options
    num_cheese = 3
    num_meat = 4
    num_veggies = 5
    
    # One of the vegetable options is peppers, which cannot be combined with pepperoni
    num_veggies_no_peppers = num_veggies - 1
    
    # If pepperoni is chosen, remove the option of peppers
    num_veggies_options = num_veggies if num_meat == 1 else num_veggies_no_peppers
    
    # Calculate the total number of topping combinations
    total_combinations = num_cheese * num_meat * num_veggies_options
    result = total_combinations
    return result

print(solution())