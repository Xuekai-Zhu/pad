def solution():
    num_customers = 100
    num_tuna = 10
    tuna_weight = 200
    serving_size = 25

    # Calculate the total amount of tuna available
    total_tuna_weight = num_tuna * tuna_weight

    # Calculate the total number of servings of tuna available
    total_servings = total_tuna_weight / serving_size

    # Calculate the number of customers who will get a serving of tuna
    num_servings = min(num_customers, total_servings)

    # Calculate the number of customers who will not get any tuna
    num_no_fish = num_customers - num_servings
    result = num_no_fish
    return result

print(solution())