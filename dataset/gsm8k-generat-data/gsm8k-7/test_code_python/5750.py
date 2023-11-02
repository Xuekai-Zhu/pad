def solution():
    sophie_oranges_per_day = 20
    hannah_grapes_per_day = 40
    num_days = 30

    # Calculate the total number of oranges that Sophie was given
    total_sophie_oranges = sophie_oranges_per_day * num_days

    # Calculate the total number of grapes that Hannah was given
    total_hannah_grapes = hannah_grapes_per_day * num_days

    # Calculate the total number of fruits that Sophie and Hannah ate
    total_fruits = total_sophie_oranges + total_hannah_grapes
    result = total_fruits
    return result

print(solution())